import styled from "styled-components";

import { MainPage } from "./pages/mainPage";

const AppWrapper = styled.div`
  width: 100%;
  height: 100rem;
`;

function App() {
  return (
    <AppWrapper>
      <MainPage />
    </AppWrapper>
  );
}

export default App;
