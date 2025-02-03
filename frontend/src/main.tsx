import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import GlobalStyles from "./styledComponents/GlobalStyles.ts";

import App from "./App.tsx";
import { CalendarPage } from "./pages/CalendarPage.tsx";

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
          <Route path="/calendar" element={<CalendarPage />} />
          <Route path="/info" />
        </Routes>
      </StrictMode>
    </BrowserRouter>
  );
}
