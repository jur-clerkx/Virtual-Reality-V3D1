using UnityEngine;

public class rotate : MonoBehaviour
{

    void Start()
    {//Set up things on the start method
    }

    float speed = 1.0f;
 
    void Update()
    {
        Vector3 move = new Vector3(Input.GetAxis("Horizontal"),0, Input.GetAxis("Vertical"));
        transform.position += move * speed * Time.deltaTime;
    }
}
