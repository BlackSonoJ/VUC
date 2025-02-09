import { FC, useEffect, useState } from 'react';
import axios from 'axios';

const getCurrentMonthAndYear = (month: number, year: number) => {
  const now = new Date(year, month);
  const options: Intl.DateTimeFormatOptions = {
    year: 'numeric',
    month: 'long',
  };
  return now.toLocaleDateString('ru-RU', options);
};

const generateCalendar = (month: number, year: number) => {
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const firstDayOfMonth = new Date(year, month, 1).getDay();
  const startDay = firstDayOfMonth === 0 ? 6 : firstDayOfMonth - 1;

  const daysArray = [];

  for (let i = 0; i < startDay; i++) {
    daysArray.push(null);
  }

  for (let day = 1; day <= daysInMonth; day++) {
    daysArray.push(day);
  }

  const totalCells = daysArray.length;
  const remainingCells = (7 - (totalCells % 7)) % 7;
  for (let i = 0; i < remainingCells; i++) {
    daysArray.push(null);
  }

  return daysArray;
};

type Events = {
  id: number;
  user: number;
  name: string;
  description: string;
  published: Date;
};

export const Calendar: FC = () => {
  const [currentMonth, setCurrentMonth] = useState(new Date().getMonth());
  const [currentYear, setCurrentYear] = useState(new Date().getFullYear());
  const [events, setEvents] = useState<Events[]>([]);
  const [selectedEvent, setSelectedEvent] = useState<Events | null>(null);

  const currentMonthAndYear = getCurrentMonthAndYear(currentMonth, currentYear);
  const currentMonthAndYearUpperCase =
    currentMonthAndYear.slice(0, 1).toUpperCase() +
    currentMonthAndYear.slice(1);
  const calendarDays = generateCalendar(currentMonth, currentYear);

  useEffect(() => {
    const handleEvents = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/events');
        console.log(response);
        if (response) {
          setEvents(response.data);
        }
      } catch (err) {
        console.error(err);
      }
    };

    handleEvents();
  }, []);

  const goToPreviousMonth = () => {
    if (currentMonth === 0) {
      setCurrentMonth(11);
      setCurrentYear(currentYear - 1);
    } else {
      setCurrentMonth(currentMonth - 1);
    }
  };

  const goToNextMonth = () => {
    if (currentMonth === 11) {
      setCurrentMonth(0);
      setCurrentYear(currentYear + 1);
    } else {
      setCurrentMonth(currentMonth + 1);
    }
  };

  const getEventForDay = (day: number | null) => {
    return events.find(event => {
      const eventDate = new Date(event.published);
      return (
        eventDate.getDate() === day &&
        eventDate.getMonth() === currentMonth &&
        eventDate.getFullYear() === currentYear
      );
    });
  };

  return (
    <div className='w-full h-fit'>
      <div className='my-5 flex justify-between items-center w-full'>
        <button
          className='text-white cursor-pointer'
          onClick={goToPreviousMonth}
        >
          ◀
        </button>
        <p className='text-white text-2xl'>{currentMonthAndYearUpperCase}</p>
        <button
          className='text-white cursor-pointer'
          onClick={goToNextMonth}
        >
          ▶
        </button>
      </div>

      <div className='grid grid-cols-7 gap-1 grid-rows-[50px_repeat(6,_200px)]'>
        {['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'].map((day, index) => (
          <div
            key={index}
            className='font-bold text-center my-2'
          >
            <p className='text-white text-lg'>{day}</p>
          </div>
        ))}
        {calendarDays.map((day, index) => {
          const event = getEventForDay(day);
          return (
            <div
              key={index}
              className={`relative flex flex-col items-center p-4 w-full h-full border border-gray-300 rounded-xl shadow-md transition-all duration-300 ${
                day ? 'bg-white hover:bg-gray-100' : 'bg-gray-200 opacity-50'
              }`}
            >
              {day && (
                <>
                  <span className='absolute top-2 left-2 text-gray-800 font-semibold text-lg'>
                    {day}
                  </span>
                  {event && (
                    <div className='mt-10 flex flex-col items-center justify-center gap-4 text-center w-[50%]'>
                      <p className='text-blue-600 font-bold text-lg w-full break-words whitespace-pre-line'>
                        {event.name}
                      </p>
                      <p className='text-gray-700 text-sm w-full break-words whitespace-pre-line'>
                        {event.description}
                      </p>
                    </div>
                  )}
                </>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
