import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import GlobalStyles from "./styledComponents/GlobalStyles.ts";

import App from "./App.tsx";

const rootElement = document.getElementById("root");

if (rootElement) {
  createRoot(rootElement).render(
    <BrowserRouter>
      <GlobalStyles />
      <StrictMode>
        <Routes>
          <Route path="*" element={<App />} />
          <Route path="/images" />
          <Route path="/videos" />
          <Route path="/calendar" />
          <Route path="/info" />
        </Routes>
      </StrictMode>
    </BrowserRouter>
  );
}
