import React from "react";
import ReactDOM from "react-dom/client";
import { setupIonicReact } from "@ionic/react";
import { BrowserRouter } from "react-router-dom";
import App from "./App";

/* Ionic Core CSS */
import "@ionic/react/css/core.css";
import "@ionic/react/css/normalize.css";
import "@ionic/react/css/structure.css";
import "@ionic/react/css/typography.css";
import "@ionic/react/css/padding.css";
import "@ionic/react/css/flex-utils.css";

/* Import custom theme */
import "./theme/custom.css";

setupIonicReact();

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
