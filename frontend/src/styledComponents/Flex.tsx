import { FC, MouseEventHandler } from "react";
import styled from "styled-components";

interface FlexProps {
  $position: "relative" | "sticky" | "absolute" | "static" | "fixed";
  $direction: "row" | "column" | "row-reverse" | "column-reverse";
  $align: "stretch" | "flex-start" | "flex-end" | "center" | "baseline";
  $justify:
    | "stretch"
    | "flex-start"
    | "flex-end"
    | "center"
    | "space-between"
    | "space-around"
    | "space-evenly";
  $wrap: "nowrap" | "wrap" | "wrap-reverse";
  $margin: string;
  $padding: string;
  $gap: string;
  width: string;
  height: string;
  $gridArea: string;
  $bgColor: string;
  $borderRadius: string;
  cursor: string;

  children: React.ReactNode;
  onClick: MouseEventHandler<HTMLDivElement>;
}

const StyledFlex = styled.div<Partial<FlexProps>>`
  position: ${(props) => props.$position || "static"};
  display: flex;
  flex-direction: ${(props) => props.$direction || "row"};
  align-items: ${(props) => props.$align || "stretch"};
  justify-content: ${(props) => props.$justify || "stretch"};
  flex-wrap: ${(props) => props.$wrap || "wrap"};
  gap: ${(props) => props.$gap || "0"};
  margin: ${(props) => props.$margin || "0"};
  padding: ${(props) => props.$padding || "0"};
  width: ${(props) => props.width || "auto"};
  height: ${(props) => props.height || "auto"};
  grid-area: ${(props) => props.$gridArea};
  background-color: ${(props) => props.$bgColor || "transparent"};
  border-radius: ${(props) => props.$borderRadius || "0"};
  cursor: ${(props) => props.cursor};
`;

export const Flex: FC<Partial<FlexProps>> = (props) => {
  return <StyledFlex {...props}>{props.children}</StyledFlex>;
};
