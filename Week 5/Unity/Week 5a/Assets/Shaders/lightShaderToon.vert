	//The uniform parameters are passed into to vertex shader
	uniform vec4 lightColor;
	uniform vec4 lightPosition;
	uniform mat4 osg_ViewMatrix;

	//These varying parameters will be passed to the fragment shader
	varying vec4 diffuseColor;
	varying vec4 ambientColor;


	/*
	This function calculates the ambient color.
	It consists of 20% of objectColor * lightColor.
	*/
	vec4 CalculateAmbientColor(vec4 objectColor, vec4 lightColor)
	{
		return lightColor * objectColor * 0.35;
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
		dotproduct = int(dotproduct / 0.333) * 0.333;
		diffuseColor = lightColor * objectColor * dotproduct;
		float deltadistance = distance(lightPositionInEyeSpace, vertexInEyeSpace);
		return diffuseColor;
	}

	void main()
	{	
		//Convert normal from object coordinates to eye coordinates
		vec3 normalinEyeSpace = normalize(gl_NormalMatrix * gl_Normal);
				//Convert vertex from object coordinate to eye coordinate
		vec4 vertexInEyeSpace = gl_ModelViewMatrix * gl_Vertex;
		
		//Lightposition is in world coordinates. It can be converted to eye coordinates by multiplying it with the view matris.
		vec4 lightPositionInEyeSpace = osg_ViewMatrix * lightPosition;
		
		ambientColor = CalculateAmbientColor(gl_FrontMaterial.diffuse , lightColor);
		diffuseColor = CalculateDiffuseColor(normalinEyeSpace, vertexInEyeSpace, lightPositionInEyeSpace, lightColor, gl_FrontMaterial.diffuse);
		
		//Converts vertex to final projection space (model viewprojection)
		gl_Position = ftransform();
	} 
