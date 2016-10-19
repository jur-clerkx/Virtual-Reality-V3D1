uniform sampler2D colorMap0;
uniform sampler2D colorMap1;
uniform float textureBlend;
varying vec2 texcoord;

void main (void)
{
	vec4 color1 = texture2D(colorMap0, texcoord) * 0.25 * (1.0 - textureBlend);
	vec4 color2 = texture2D(colorMap1, texcoord) * 0.25 * textureBlend;
	gl_FragColor = color1 + color2;
}