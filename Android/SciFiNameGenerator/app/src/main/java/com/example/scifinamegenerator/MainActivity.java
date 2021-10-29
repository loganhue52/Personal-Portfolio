package com.example.scifinamegenerator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    //defining the widget variables
    EditText firstTXT;
    EditText lastTXT;
    EditText cityTXT;
    EditText schoolTXT;
    EditText broTXT;
    EditText sisTXT;
    Button genBTN;
    TextView output;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        firstTXT = findViewById(R.id.firstTXT);
        lastTXT = findViewById(R.id.lastTXT);
        cityTXT = findViewById(R.id.cityTXT);
        schoolTXT = findViewById(R.id.schoolTXT);
        broTXT = findViewById(R.id.broTXT);
        sisTXT = findViewById(R.id.sisTXT);
        output = findViewById(R.id.output);
        genBTN = findViewById(R.id.genBTN);

        //utilize an onClickListener to lsiten for the button
        genBTN.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                generate();
            }

        });
    }

    private void generate(){
        String first = String.valueOf(firstTXT.getText());
        String last = String.valueOf(lastTXT.getText());
        String city = String.valueOf(cityTXT.getText());
        String school = String.valueOf(schoolTXT.getText());
        String bro = String.valueOf(broTXT.getText());
        String sis = String.valueOf(sisTXT.getText());

        int rF = (int) (Math.random()*first.length());
        int rL = (int) (Math.random()*last.length());
        int rC = (int) (Math.random()*city.length());
        int rS = (int) (Math.random()*school.length());
        int rB = (int) (Math.random()*bro.length());
        int rSi = (int) (Math.random()*sis.length());

        String sciFiFirst = first.substring(0,rF)+last.substring(rL);
        String sciFiLast = city.substring(0,rC)+school.substring(rS);
        String sciFiHome = bro.substring(rB)+sis.substring(0,rSi);

        output.setText(String.format("Welcome %s %s from %s",sciFiFirst,sciFiLast,sciFiHome));
    }
}