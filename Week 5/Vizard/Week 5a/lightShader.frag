//The varying parameters are passed from the vertex shader to this fragment shader
varying vec4 diffuseColor;
varying vec4 ambientColor;
varying vec4 specularColor;

	
	void main()
	{
		//Assign the ambientColor + diffuseColor to the final color to be displayed (gl_FragColor)
		gl_FragColor = ambientColor + diffuseColor + specularColor;
	}

