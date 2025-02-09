import { FC, useEffect, useState } from 'react';
import HeaderComponent from '../styledComponents/Header';
import { Clock } from './Clock';
import { DateBlock } from './Date';
import { MainPageButton } from './MainPageButton';
import Grid from '../styledComponents/Grid';
import { MenuButton } from './MenuButton';
import { Link, useLocation } from 'react-router-dom';

export const Header: FC = () => {
  const [buttonText, setButtonText] = useState<string>('');
  const location = useLocation();

  useEffect(() => {
    if (location.pathname === '/') {
      setButtonText('Вы на главной');
    } else {
      setButtonText('Назад на главную');
    }
  }, [location.pathname]);

  return (
    <HeaderComponent
      $width='100%'
      $height='150px'
      $margin='0 0 7px 0'
    >
      <Grid>
        <DateBlock />
        <Clock />
        <MainPageButton buttonText={buttonText} />
        <Link
          to='/videos'
          style={{
            gridArea: '1 / 3 / 2 / 4',
            backgroundColor: '#2b41fe',
            textDecoration: 'none',
            borderRadius: '3px',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <MenuButton
            text='Видеоматериалы'
            margin='0 5px 5px 0'
          />
        </Link>
        <Link
          to='/images'
          style={{
            gridArea: '1 / 4 / 2 / 5',
            backgroundColor: '#2b41fe',
            textDecoration: 'none',
            borderRadius: '3px',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <MenuButton
            text='Фотоматериалы'
            margin='0 0 5px 0'
          />
        </Link>
        <Link
          to='/calendar'
          style={{
            gridArea: '2 / 3 / 3 / 4',
            backgroundColor: '#2b41fe',
            textDecoration: 'none',
            borderRadius: '3px',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <MenuButton text='Календарь событий' />
        </Link>
        <Link
          to='/info'
          style={{
            gridArea: '2 / 4 / 3 / 5',
            backgroundColor: '#2b41fe',
            textDecoration: 'none',
            borderRadius: '3px',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <MenuButton text='Информация' />
        </Link>
      </Grid>
    </HeaderComponent>
  );
};
