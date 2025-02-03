import { FC } from "react";
import { Flex } from "../styledComponents/Flex";
import { Image } from "../styledComponents/Image";
import { Container } from "../styledComponents/Container";

export const Content: FC = () => {
  return (
    <Container $width="100%" height="100%">
      <Flex
        width="100%"
        height="100%"
        $justify="center"
        $align="center"
        $border="10px solid #3b04c67c"
        $boxShadow="0 0 0 2px white"
        $borderRadius="5px"
      >
        <Image
          width="100%"
          $cover="cover"
          height="fit-content"
          src="../../public/mem.jpg"
        />
      </Flex>
    </Container>
  );
};
