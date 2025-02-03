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
      width="250px"
      $borderTop="1px solid white"
      $gridArea="2 / 1 / 3 / 3"
    >
      <Paragraph $fontSize="4rem">{time.toLocaleTimeString()}</Paragraph>
    </Container>
  );
};
