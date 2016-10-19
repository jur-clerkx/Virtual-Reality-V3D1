// Upgrade NOTE: replaced '_Object2World' with 'unity_ObjectToWorld'
// Upgrade NOTE: replaced '_World2Object' with 'unity_WorldToObject'

Shader "Lit/Diffuse With Ambient"
{
	Properties
	{
		_DiffuseColor("Diffuse Material Color", Color) = (1,1,1,1)
		_AmbientColor("Ambient Material Color", Color) = (1,1,1,1)
		_LightColor("Light Color", Color) = (1,1,1,1)
		_FadeDistance("Fade Distance", Float) = 5
		_SpecularColor("Specular Light Coolor", Color) = (1,1,1,1)
		_Shininess("Shininess", Float) = 10
		_FogStarting("Fog Start Distance", Float) = 0.5
		_FogEnding("Fog Ending Distance", Float) = 10
	}
		SubShader
	{
		Pass
	{
		Tags{ "LightMode" = "ForwardBase" }

		CGPROGRAM
#pragma vertex vert
#pragma fragment frag
#include "UnityCG.cginc"
#include "UnityLightingCommon.cginc"
	uniform fixed4 _DiffuseColor;
	uniform fixed4 _AmbientColor;
	uniform fixed4 _LightColor;
	uniform float _FadeDistance;
	uniform float _FogStarting;
	uniform float _FogEnding;
	uniform fixed4 _SpecularColor;
	uniform float _Shininess;
	struct v2f
	{
		fixed4 diff : COLOR0;
		fixed4 amb : COLOR1;
		fixed4 spec : COLOR2;
		float4 vertex : SV_POSITION;
	};

	v2f vert(appdata_base v)
	{

		v2f o;
		o.vertex = UnityObjectToClipPos(v.vertex);

		//Calculate part
		float4 lightPosition = float4(0, 0, 3, 1.0);
		float4 lightColor = _LightColor;
		float4 posWorld = mul(unity_ObjectToWorld, v.vertex);
		float3 vertexToLightSource = lightPosition.xyz - posWorld.xyz;
		float3 lightDirection = normalize(vertexToLightSource);
		float squaredDistance =	dot(vertexToLightSource, vertexToLightSource);
		float3 normalDir = normalize(mul(float4(v.normal, 0.0), unity_WorldToObject).xyz);
		float4 diffuseReflection = _DiffuseColor * lightColor * max(0.0, dot(normalDir, lightDirection));
		float4 specularReflection = _SpecularColor * pow(max(0.0, dot(normalDir, normalize(normalize(-posWorld.xyz) + lightDirection.xyz))), _Shininess);
		

		// the only difference from previous shader:
		// in addition to the diffuse lighting from the main light,
		// add illumination from ambient or light probes
		// ShadeSH9 function from UnityCG.cginc evaluates it,
		// using world space normal
		//o.diff.rgb += ShadeSH9(half4(worldNormal,1));
		////////////Fog Effect
		float eyeDistance = length(o.vertex.xyz);
		float fogFactor = (_FogEnding - eyeDistance) / (_FogEnding - _FogStarting);
		o.diff = diffuseReflection * fogFactor;// *(1 - distance(lightPosition, posWorld) / _FadeDistance);
		o.amb = _AmbientColor * 0.2 * fogFactor;
		o.spec = specularReflection * fogFactor;// *(1 - distance(lightPosition, posWorld) / _FadeDistance);
		return o;
	}

	sampler2D _MainTex;

	fixed4 frag(v2f i) : SV_Target
	{
		fixed4 col = i.amb + i.diff + i.spec;
		////////////Toon effect:
		//col.x = max(i.amb.x, float(int(col.x / 0.2)) * 0.2);
		//col.y = max(i.amb.y, float(int(col.y / 0.2)) * 0.2);
		//col.z = max(i.amb.z, float(int(col.z / 0.2)) * 0.2);
		//col.w = max(i.amb.w, float(int(col.w / 0.2)) * 0.2);
		return col;
	}
		ENDCG
	}
	}
}