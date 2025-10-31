import React from "react";
import {
  IonApp,
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonButton,
  IonFooter,
  IonGrid,
  IonRow,
  IonCol,
} from "@ionic/react";
import { Route, Routes, useNavigate, useLocation } from "react-router-dom";

import TextAudio from "./pages/TextAudio";
import AudioAudio from "./pages/AudioAudio";
import ImageAudio from "./pages/ImageAudio";

const App: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const getActive = (path: string) => (location.pathname === path ? "active-btn" : "");

  return (
    <IonApp>
      <IonPage>
        {/* HEADER BAR */}
        <IonHeader>
          <IonToolbar color="light" className="custom-toolbar">
           
            <IonTitle color="dark" className="ion-text-center">
               Audio Steganography
            </IonTitle>

          </IonToolbar>
        </IonHeader>

        {/* MAIN CONTENT */}
        <IonContent fullscreen className="ion-padding custom-bg">
 

          {/* Route Content */}
          <Routes>
            <Route path="/" element={<TextAudio />} />
            <Route path="/text-audio" element={<TextAudio />} />
            <Route path="/audio-audio" element={<AudioAudio />} />
            <Route path="/image-audio" element={<ImageAudio />} />
          </Routes>
        </IonContent>

        {/* FOOTER NAVIGATION */}
        <IonFooter className="footer-nav">
          <IonGrid>
            <IonRow className="ion-justify-content-center ion-align-items-center">
              <IonCol size="auto">
                <IonButton
                  fill="clear"
                  shape="round"
                  className={`nav-btn ${getActive("/")}`}
                  onClick={() => navigate("/")}
                >
                  ❶
                </IonButton>
              </IonCol>
              <IonCol size="auto">
                <IonButton
                  fill="clear"
                  shape="round"
                  className={`nav-btn ${getActive("/audio-audio")}`}
                  onClick={() => navigate("/audio-audio")}
                >
                  ❷
                </IonButton>
              </IonCol>
              <IonCol size="auto">
                <IonButton
                  fill="clear"
                  shape="round"
                  className={`nav-btn ${getActive("/image-audio")}`}
                  onClick={() => navigate("/image-audio")}
                >
                  ❸
                </IonButton>
              </IonCol>
            </IonRow>
          </IonGrid>
        </IonFooter>
      </IonPage>
    </IonApp>
  );
};

export default App;
