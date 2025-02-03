import { FC } from "react";
import styled from "styled-components";

interface ContainerProps {
  $textAlign: string;
  $fontWeight: string;
  $position: "relative" | "sticky" | "absolute" | "static" | "fixed";
  $top: string;
  $bottom: string;
  $right: string;
  display: string;
  $justify: string;
  $align: string;
  $width: string;
  $height: string;
  $maxWidth: string;
  height: string;
  $margin: string;
  $padding: string;
  $bgColor: string;
  $borderRadius: string;
  $border: string;
  $borderBottom: string;
  $borderTop: string;
  $boxShadow: string;
  $zIndex: number;
  cursor: string;
  $gridArea: string;
  $gridTemplateColumns: string;
  $gridTemplateRows: string;
  $gap: string;
  children: React.ReactNode;

  onClick: () => void;
  className: string;
}

const StyledContainer = styled.div<Partial<ContainerProps>>`
  text-align: ${(props) => props.$textAlign};
  font-weight: ${(props) => props.$fontWeight};
  position: ${(props) => props.$position || "static"};
  ${(props) => props.$top && `top: ${props.$top};`}
  ${(props) => props.$bottom && `bottom: ${props.$bottom};`}
  ${(props) => props.$right && `right: ${props.$right};`}
  display: ${(props) => props.display || "block"};
  ${(props) => props.$justify && `justify-content: ${props.$justify};`}
  ${(props) => props.$align && `align-items: ${props.$align};`}
  width: ${(props) => props.$width || "auto"};
  height: ${(props) => props.$height};
  max-width: ${(props) => props.$width};
  padding: ${(props) => props.$padding || "0"};
  height: ${(props) => props.height || "auto"};
  margin: ${(props) => props.$margin || "0"};
  background-color: ${(props) => props.$bgColor || "transparent"};
  border: ${(props) => props.$border};
  border-radius: ${(props) => props.$borderRadius || "0"};
  border-top: ${(props) => props.$borderTop || "none"};
  border-bottom: ${(props) => props.$borderBottom || "none"};
  box-shadow: ${(props) => props.$boxShadow || "none"};
  z-index: ${(props) => props.$zIndex || "0"};
  grid-area: ${(props) => props.$gridArea};
  grid-template-columns: ${(props) => props.$gridTemplateColumns};
  grid-template-rows: ${(props) => props.$gridTemplateRows};
  gap: ${(props) => props.$gap};
  cursor: ${(props) => props.cursor};
`;

export const Container: FC<Partial<ContainerProps>> = (props) => {
  return <StyledContainer {...props}>{props.children}</StyledContainer>;
};
