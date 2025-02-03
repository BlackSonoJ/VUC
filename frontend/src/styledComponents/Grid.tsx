import styled from "styled-components";

const Grid = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 5px;
  grid-row-gap: 5px;
  width: 100%;
  height: 150px;

  & > *:nth-child(1),
  & > *:nth-child(2) {
    margin-bottom: -5px;
  }
`;

export default Grid;
