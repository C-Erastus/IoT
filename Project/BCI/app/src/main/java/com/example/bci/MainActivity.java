package com.example.bci;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.EventListener;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;
import com.google.firebase.firestore.proto.TargetGlobal;

import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    public static final String ACTION_KEY = "action";

    public static final String ANAME_KEY = "Action Name";
    public static final String STATUS_KEY = "Status";

    TextView textView;

    private DocumentReference myDocRef = FirebaseFirestore.getInstance().document("MobleIoT/Actions");
    private DocumentReference resDocRef = FirebaseFirestore.getInstance().document("MobleIoT/Results");
    private String TAG;

    @Override
    protected void onStart(){
        super.onStart();
        resDocRef.addSnapshotListener(this, new EventListener<DocumentSnapshot>() {
            @Override
            public void onEvent(@Nullable DocumentSnapshot documentSnapshot, @Nullable FirebaseFirestoreException e) {
                if(documentSnapshot.exists()){
                    String actionText = documentSnapshot.getString(ANAME_KEY);
                    String statusText = documentSnapshot.getString(STATUS_KEY);
                    textView.setText("\"" + actionText + "\"\n" + statusText);
                }
            }
        });
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void saveAction(View view){ // an onClick handler
        //TODO: fill this out
        EditText actionView = (EditText) findViewById(R.id.editText); // get the text entered in the edit text;
        ((EditText) findViewById(R.id.editText)).setTextColor(Color.WHITE);
        String actionText = actionView.getText().toString(); // get strings from the text.

        if (actionText.isEmpty()){return;}
        Map<String, Object> dataToSave = new HashMap<String, Object>();
        dataToSave.put(ACTION_KEY, actionText); // the data in the database will be saved in a map as a key value pair
        myDocRef.set(dataToSave).addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()){
                    Log.d(TAG, "The data was saved in the Document");
                }else{
                    Log.w(TAG, "data wasn't saved", task.getException());
                }
            }
        });
    }
}
