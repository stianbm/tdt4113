// Constants and variables (...Mr. Dewitt)
const int greenPin = 8;
const int yellowPin = 6;
const int bluePin = 4;
const int buttonPin = 2;

const int dotSignal = 1;
const int dashSignal = 2;
const int letterPauseSignal = 3;
const int wordPauseSignal = 4;

const int T = 500;
const int letterPause = 3*T;
const int wordPause = 7*T;

int buttonState = HIGH;    // LOW means pressed / active
int previousState = HIGH;
long buttonPress = 0;
long buttonRelease = 0;
long deltaT = 0;
bool wordPauseSent = false;


void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);
  
  pinMode(greenPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(buttonPin, INPUT);
  
  digitalWrite(greenPin, LOW);
  digitalWrite(yellowPin, LOW);
  digitalWrite(bluePin, LOW);
}


void loop() {
  // put your main code here, to run repeatedly:

  buttonState = digitalRead(buttonPin);

  // Pressed event
  if(buttonState == LOW && previousState == HIGH){
    wordPauseSent = false;
    previousState = LOW;
    buttonPress = millis();

    // Handle pause
    deltaT = buttonPress - buttonRelease;
    
    if(deltaT > letterPause && deltaT < wordPause){
      Serial.print(letterPauseSignal);
    }
  }

  // Released event
  else if(buttonState == HIGH && previousState == LOW){
    previousState = HIGH;
    buttonRelease = millis();

    // Handle signal length
    deltaT = buttonRelease - buttonPress;
    if(deltaT > T){
      Serial.print(dashSignal);
    }
    else{
      Serial.print(dotSignal);
    }
  }

  // Work indicators pause
  else if(buttonState == HIGH){
    deltaT = millis() - buttonRelease;
    if(deltaT > wordPause && !wordPauseSent){
      setGreen();
      Serial.print(wordPauseSignal);
      wordPauseSent = true;
    }
    else if(deltaT > wordPause){
      setGreen();
    }
    else if(deltaT > letterPause){
      setYellow();
    }
    else{
      setBlue();
    }
  }

  // Work indicators press
  else if(buttonState == LOW){
    deltaT = millis() - buttonPress;
    if(deltaT > T){
      setYellow();
    }
    else{
      setBlue();
    }
  }
}

void setYellow(){
  digitalWrite(yellowPin, HIGH);
  digitalWrite(greenPin, LOW);
  digitalWrite(bluePin, LOW);
}

void setGreen(){
  digitalWrite(yellowPin, LOW);
  digitalWrite(greenPin, HIGH);
  digitalWrite(bluePin, LOW);
}

void setBlue(){
  digitalWrite(yellowPin, LOW);
  digitalWrite(greenPin, LOW);
  digitalWrite(bluePin, HIGH);
}
