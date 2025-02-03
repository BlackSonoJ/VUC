import { createGlobalStyle } from "styled-components";

const GlobalStyles = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html,body, #root {
  width:100%;
  height: fit-content;
  font-family: "Noto Sans JP", sans-serif;
  font-optical-sizing: auto;
  font-weight: 300;
  font-style: normal;
  padding: 4px;
  background-color: #000040;
  }
`;

export default GlobalStyles;
