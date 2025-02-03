import { FC, useEffect, useState } from "react";
import { Container } from "../styledComponents/Container";
import { Paragraph } from "../styledComponents/Paragraph";

export const Clock: FC = () => {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const interval = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <Container
      $width="100%"
      $borderTop="2px solid #0f0f81"
      $bgColor="#0c0c23"
      $gridArea="2 / 1 / 3 / 2"
    >
      <Paragraph $fontSize="4rem">{time.toLocaleTimeString()}</Paragraph>
    </Container>
  );
};
