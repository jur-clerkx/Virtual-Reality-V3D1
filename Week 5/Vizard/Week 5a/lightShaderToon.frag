//The varying parameters are passed from the vertex shader to this fragment shader
varying vec4 diffuseColor;
varying vec4 ambientColor;

	
	void main()
	{
		//Assign the ambientColor + diffuseColor to the final color to be displayed (gl_FragColor)
		vec4 fullColor = ambientColor + diffuseColor;
		fullColor.x = max(0.1, float(int(fullColor.x / 0.2)) * 0.2);
		fullColor.y = max(0.1, float(int(fullColor.y / 0.2)) * 0.2);
		fullColor.z = max(0.1, float(int(fullColor.z / 0.2)) * 0.2);
		fullColor.w = max(0.1, float(int(fullColor.w / 0.2)) * 0.2);
		gl_FragColor = fullColor;
	}

