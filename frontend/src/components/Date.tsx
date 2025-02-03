import { FC } from "react";
import { Container } from "../styledComponents/Container";
import { Paragraph } from "../styledComponents/Paragraph";

export const DateBlock: FC = () => {
  const today = new Date();

  return (
    <Container>
      <Paragraph $fontSize="64px">{today.toLocaleDateString()}</Paragraph>
    </Container>
  );
};
