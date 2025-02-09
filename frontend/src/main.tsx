import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import './style.css';
import GlobalStyles from './styledComponents/GlobalStyles.ts';

import App from './App.tsx';
import { CalendarPage } from './pages/CalendarPage.tsx';
import { VideosPage } from './pages/VideosPage.tsx';
import { ImagesPage } from './pages/ImagesPage.tsx';
import { InfoPage } from './pages/InfoPage.tsx';

const rootElement = document.getElementById('root');

if (rootElement) {
  createRoot(rootElement).render(
    <BrowserRouter>
      <GlobalStyles />
      <StrictMode>
        <Routes>
          <Route
            path='*'
            element={<App />}
          />
          <Route
            path='/images'
            element={<ImagesPage />}
          />
          <Route
            path='/videos'
            element={<VideosPage />}
          />
          <Route
            path='/calendar'
            element={<CalendarPage />}
          />
          <Route
            path='/info'
            element={<InfoPage />}
          />
        </Routes>
      </StrictMode>
    </BrowserRouter>
  );
}
