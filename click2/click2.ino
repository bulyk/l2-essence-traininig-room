#include <Mouse.h>
#include <Keyboard.h>

int incomingByte;
int x_coord = 0;
int y_coord = 0;
int nul = -100;


void setup(){
  Serial.begin(9600);
  Serial.setTimeout(5);

}


void loop(){

  if(Serial.available())
  {
    char key = Serial.read();
    int val = Serial.parseInt();
    switch (key)
    {
      case 'x': x_coord = val;
      // Serial.println(x_coord); 
      break;

      case 'y': y_coord = val;
      // Serial.println(y_coord); 
      break;
      
      //ДВИЖЕНИЕ ПО У
      case 'n': y_coord = val; 
      for (int a = 1; a < 0.79*y_coord; a++)
      {
      Mouse.move(0, 2);
      }
      delay(500);
      break;
      
      //ДВИЖЕНИЕ ПО Х
      case 'm': x_coord = val; 
      for (int a = 1; a < 0.79*x_coord; a++)
      {
      Mouse.move(2, 0);
      }
      delay(500);
      break;

      case 'o': 
      for (int i = 0; i < 10; i++)
      {
      Mouse.move(nul, nul);
      // Serial.println(y_coord); 
      }
      delay(500);
      
      break;
      
      case 'c': Mouse.click();
      // Serial.println(y_coord); 
      delay(500);
      break;

      case 'z': 
      Keyboard.press('z');
      Keyboard.releaseAll();
      // Serial.println(y_coord); 
      delay(500);
      break;

    }
    // switch (key)
    // {
    //   case 'x': x_coord = val;
    //   // Serial.println(x_coord); 
    //   break;
    //   case 'y': y_coord = val;
    //   // Serial.println(y_coord); 
    //   break;
    // }
    Serial.println(x_coord); 
    Serial.println(y_coord); 

  }

}