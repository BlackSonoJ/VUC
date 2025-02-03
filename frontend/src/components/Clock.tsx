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
    <Container>
      <Paragraph $fontSize="64px">{time.toLocaleTimeString()}</Paragraph>
    </Container>
  );
};
