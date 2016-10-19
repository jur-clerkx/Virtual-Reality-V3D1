	//The uniform parameters are passed into to vertex shader
	uniform vec4 lightColor;
	uniform vec4 lightPosition;
	uniform mat4 osg_ViewMatrix;
	uniform float shininess;
	uniform float fogStart;
	uniform float fogEnd;

	//These varying parameters will be passed to the fragment shader
	varying vec4 diffuseColor;
	varying vec4 ambientColor;
	varying vec4 specularColor;


	/*
	This function calculates the ambient color.
	It consists of 20% of objectColor * lightColor.
	*/
	vec4 CalculateAmbientColor(vec4 objectColor, vec4 lightColor)
	{
		return lightColor * objectColor * 0.1;
	}
	
	/*
	This function calculates the diffuse color
	- Intensity is decreased in a linear fashion betweeen lightsource and vertex
	  i.e. a distance of 0 = 100% intensity, and a distance of 10 or more = 0% intensity.
	- Intensity also depends on the angle that the light hits the vertex.
	*/
	vec4 CalculateDiffuseColor(
				vec3 normalInEyeSpace,
				vec4 vertexInEyeSpace,
				vec4 lightPositionInEyeSpace,
				vec4 lightColor,
				vec4 objectColor)
	{
		vec4 angle = normalize(lightPositionInEyeSpace - vertexInEyeSpace);
		float dotproduct = dot(angle, vec4(normalInEyeSpace, 0));
		if (dotproduct < 0) {
			dotproduct = 0;
		}
		diffuseColor = lightColor * objectColor * dotproduct;
		float deltadistance = distance(lightPositionInEyeSpace, vertexInEyeSpace);
		diffuseColor = diffuseColor * vec4((1 - deltadistance / 100));
		return diffuseColor;
	}
	
	/*
	This function calculates the specular color
	*/
	vec4 CalculateSpecularColor(
				vec3 normalInEyeSpace,
				vec4 vertexInEyeSpace,
				vec4 lightPositionInEyeSpace,
				vec4 objectColor,
				float shininess)
	{
		vec3 lightDirection = lightPositionInEyeSpace.xyz - vertexInEyeSpace.xyz;
		float lightDistance = length(lightDirection);
		lightDirection = normalize(lightDirection);
	
		//The 'eye' is at the vertex projected in eye space.
		vec3 eyeDirection = normalize(-vertexInEyeSpace.xyz);
		
		//The halfvector is the reflection between lightdirection vector and eye vector.
		vec3 halfVector = normalize(lightDirection + eyeDirection);

		float dotproduct = dot(halfVector, normalInEyeSpace);
		if (dotproduct < 0) {
			dotproduct = 0;
		}
		dotproduct = pow(dotproduct, shininess);
		vec4 lightColor = (1,1,1,1);
		specularColor = lightColor * objectColor * dotproduct;
		specularColor = specularColor * (1 - lightDistance / 5);
		return specularColor;
	}

	void main()
	{	
		//Convert normal from object coordinates to eye coordinates
		vec3 normalinEyeSpace = normalize(gl_NormalMatrix * gl_Normal);
		//Convert vertex from object coordinate to eye coordinate
		vec4 vertexInEyeSpace = gl_ModelViewMatrix * gl_Vertex;
		
		float fogFactor = (fogEnd - length(vertexInEyeSpace)) / (fogEnd - fogStart);
		
		//Lightposition is in world coordinates. It can be converted to eye coordinates by multiplying it with the view matris.
		vec4 lightPositionInEyeSpace = osg_ViewMatrix * lightPosition;
		
		ambientColor = CalculateAmbientColor(gl_FrontMaterial.diffuse , lightColor);// * fogFactor;
		diffuseColor = CalculateDiffuseColor(normalinEyeSpace, vertexInEyeSpace, lightPositionInEyeSpace, lightColor, gl_FrontMaterial.diffuse);// * fogFactor;
		specularColor = CalculateSpecularColor(normalinEyeSpace, vertexInEyeSpace, lightPositionInEyeSpace, gl_FrontMaterial.diffuse, shininess);// * fogFactor;
		
		//Converts vertex to final projection space (model viewprojection)
		gl_Position = ftransform();
	} 
