import React, { FC } from 'react';
import styled from 'styled-components';

interface PragraphProps {
  color?: string;
  $wrap?: string;
  $maxLines?: number;
  $width?: string;
  $height?: string;
  $fontSize?: string;
  $textAlign?: string;
  $margin?: string;
  children: React.ReactNode;
}

const StyledParagraph = styled.p<PragraphProps>`
  color: ${props => props.color || 'white'};
  font-size: ${props => props.$fontSize || '12px'};
  white-space: ${props => props.$wrap || 'normal'};
  width: ${props => props.$width || 'auto'};
  height: ${props => props.$height || 'auto'};
  text-align: ${props => props.$textAlign || 'center'};
  overflow: hidden;
  overflow-wrap: break-word;
  word-wrap: break-word;
  margin: ${props => props.$margin};
`;

export const Paragraph: FC<PragraphProps> = props => {
  return <StyledParagraph {...props}>{props.children}</StyledParagraph>;
};
