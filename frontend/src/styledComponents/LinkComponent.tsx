import styled from "styled-components";
import { Link } from "react-router-dom";

interface StyledLinkProps {
  display: string;
  $justify: string;
  $align: string;
  $bgColor: string;
  $borderRadius: string;
  $margin: string;
}

export const StyledLink = styled(Link)<Partial<StyledLinkProps>>`
  background-color: ${(props) => props.$bgColor || "#2b41fe"};
  text-decoration: none;
  border-radius: ${(props) => props.$borderRadius || "3px"};
  display: ${(props) => props.display};
  justify-content: ${(props) => props.$justify};
  align-items: ${(props) => props.$align};
  margin: ${(props) => props.$margin || "0"};
`;
