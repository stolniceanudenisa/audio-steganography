import React, { useState } from "react";
import {
  IonPage,
  IonGrid,
  IonRow,
  IonCol,
  IonCard,
  IonCardHeader,
  IonCardTitle,
  IonCardContent,
  IonButton,
  IonInput,
  IonTextarea,
  IonItem,
  IonLabel,
  IonLoading,
} from "@ionic/react";
import axios from "axios";
import "./textaudio.css";
const API_BASE = "http://127.0.0.1:8000/v1";

const TextAudio: React.FC = () => {
  const [secretText, setSecretText] = useState("");
  const [audioFile, setAudioFile] = useState<File | null>(null);
  const [decodedFile, setDecodedFile] = useState<File | null>(null);
  const [decodedText, setDecodedText] = useState("");
  const [loading, setLoading] = useState(false);

  const handleEncode = async () => {
    if (!audioFile || !secretText.trim()) return alert("Upload audio & text");
    const formData = new FormData();
    formData.append("file", audioFile);
    formData.append("secret_text", secretText);
    formData.append("algorithm", "LSB");

    try {
      setLoading(true);
      const res = await axios.post(`${API_BASE}/encode-text`, formData, {
        responseType: "blob",
      });
      const blobUrl = window.URL.createObjectURL(res.data);
      const a = document.createElement("a");
      a.href = blobUrl;
      a.download = "encoded.wav";
      a.click();
    } catch (err) {
      alert("Encoding failed.");
    } finally {
      setLoading(false);
    }
  };

  const handleDecode = async () => {
    if (!decodedFile) return alert("Upload a stego audio file");
    const formData = new FormData();
    formData.append("file", decodedFile);
    formData.append("algorithm", "LSB");

    try {
      setLoading(true);
      const res = await axios.post(`${API_BASE}/decode-text`, formData);
      setDecodedText(res.data.secret_text);
    } catch {
      alert("Decoding failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <IonPage>
      <IonLoading isOpen={loading} message="Processing..." />
      <IonGrid className="split-grid">
        <IonRow>
          {/* LEFT - ENCODE */}
 
            <IonCol size="12" sizeMd="6" className="encode-col">

            <IonCard className="split-card">
              <IonCardHeader>
                <IonCardTitle> Encode Text → Audio</IonCardTitle>
              </IonCardHeader>
              <IonCardContent>
                
                
  <IonItem>
  <IonLabel position="stacked">Upload Audio (.wav)</IonLabel>
  <div className="file-upload">
    <label htmlFor="encode-audio" className="upload-btn">
       Choose File
    </label>
    <input
      id="encode-audio"
      type="file"
      accept="audio/wav"
      onChange={(e) =>
        setAudioFile(e.target.files ? e.target.files[0] : null)
      }
    />
    {audioFile && (
      <span className="file-name">{audioFile.name}</span>
    )}
  </div>
    </IonItem>



<IonItem className="secret-text-item">
  <IonLabel position="stacked">Secret Text</IonLabel>
  <IonTextarea
    placeholder="Enter secret message..."
    rows={4}
    value={secretText}
    onIonChange={(e) => setSecretText(e.detail.value!)}
  />
</IonItem>

                {audioFile && (
                  <audio
                    controls
                    src={URL.createObjectURL(audioFile)}
                    style={{ marginTop: "10px", width: "100%" }}
                  />
                )}

                <IonButton expand="block" className="ion-margin-top" onClick={handleEncode}>
                  Encode & Download
                </IonButton>
              </IonCardContent>
            </IonCard>
          </IonCol>

          {/* RIGHT - DECODE */}
         
          <IonCol size="12" sizeMd="6" className="decode-col">
            <IonCard className="split-card">
              <IonCardHeader>
                <IonCardTitle> Decode Audio → Text</IonCardTitle>
              </IonCardHeader>
              <IonCardContent>
<IonItem>
  <IonLabel position="stacked">Upload Stego Audio</IonLabel>
  <div className="file-upload">
    <label htmlFor="decode-audio" className="upload-btn">
      🎧 Choose File
    </label>
    <input
      id="decode-audio"
      type="file"
      accept="audio/wav"
      onChange={(e) =>
        setDecodedFile(e.target.files ? e.target.files[0] : null)
      }
    />
    {decodedFile && (
      <span className="file-name">{decodedFile.name}</span>
    )}
  </div>
</IonItem>


                {decodedFile && (
                  <audio
                    controls
                    src={URL.createObjectURL(decodedFile)}
                    style={{ marginTop: "10px", width: "100%" }}
                  />
                )}

                <IonButton expand="block" className="ion-margin-top" onClick={handleDecode}>
                  Decode Text
                </IonButton>

                {decodedText && (
                  <IonItem style={{ marginTop: "10px" }}>
                    <IonLabel position="stacked">Decoded Message</IonLabel>
                    <IonTextarea value={decodedText} readonly rows={4} />
                  </IonItem>
                )}
              </IonCardContent>
            </IonCard>
          </IonCol>
        </IonRow>
      </IonGrid>
    </IonPage>
  );
};

export default TextAudio;
