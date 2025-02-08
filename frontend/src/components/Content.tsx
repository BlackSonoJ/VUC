import { FC, useEffect, useState } from 'react';
import { Flex } from '../styledComponents/Flex';
import { Image } from '../styledComponents/Image';
import { Container } from '../styledComponents/Container';
import axios from 'axios';

type ImgType = {
  id: number;
  image: string;
};

export const Content: FC = () => {
  const [images, setImages] = useState<ImgType[]>([]);

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/images/')
      .then(response => {
        if (Array.isArray(response.data)) {
          setImages(response.data);
        } else {
          console.error('Response data is not an array:', response.status);
        }
      })
      .catch(err => console.error(err));
  }, []);

  return (
    <Container
      $width='100%'
      height='100%'
    >
      <Flex
        width='100%'
        height='100%'
        $justify='center'
        $align='center'
        $border='10px solid #3b04c67c'
        $boxShadow='0 0 0 2px white'
        $borderRadius='5px'
      >
        {images.length > 0 && (
          <Image
            width='100%'
            $cover='cover'
            height='fit-content'
            src={images[0].image}
          />
        )}
      </Flex>
    </Container>
  );
};
