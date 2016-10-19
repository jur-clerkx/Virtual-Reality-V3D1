using UnityEngine;
using System.Collections;

public class ToggleFog : MonoBehaviour {
    bool down = false;
    int mode = 0;
	// Use this for initialization
	void Start () {
        RenderSettings.fog = true;
        RenderSettings.fogMode = FogMode.Linear;
        RenderSettings.fogStartDistance = 2;
        RenderSettings.fogEndDistance = 15;
        RenderSettings.fogDensity = 0.2f;
        RenderSettings.fogColor = Color.red;
	}
	
	// Update is called once per frame
	void Update () {
	    if(Input.GetKey("space"))
        {
            if (!down)
            {
                if (mode == 0)
                {
                    mode = 1;
                    RenderSettings.fogMode = FogMode.Exponential;
                } else if (mode == 1)
                {
                    mode = 2;
                    RenderSettings.fog = false;
                } else if (mode == 2)
                {
                    mode = 0;
                    RenderSettings.fog = true;
                    RenderSettings.fogMode = FogMode.Linear;
                }
                down = true;
            }
        } else
        {
            down = false;
        }
	}
}
