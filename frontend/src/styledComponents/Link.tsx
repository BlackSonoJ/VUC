import { FC } from "react";
import styled from "styled-components";

interface LinkProps {
  href: string;
  $decoration: "underline" | "none" | "overline red";
  $width: string;
  $height: string;
  color: string;
  $gridArea: string;
  children: React.ReactNode;
}

const StyledLink = styled.a<Partial<LinkProps>>`
  text-decoration: ${(props) => props.$decoration};
  width: ${(props) => props.$width};
  height: ${(props) => props.$height};
  color: ${(props) => props.color};
  grid-area: ${(props) => props.$gridArea};
`;

export const Link: FC<Partial<LinkProps>> = (props) => {
  const { href, children, ...rest } = props;
  return (
    <StyledLink href={href} {...rest}>
      {children}
    </StyledLink>
  );
};
