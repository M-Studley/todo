'use client';
import React, { useState } from 'react';
import {
  CheckCircleIcon,
  EllipsisVerticalIcon,
} from '@heroicons/react/24/outline';
import {
  Button,
  Card,
  CardBody,
  Dropdown,
  DropdownItem,
  DropdownMenu,
  DropdownTrigger,
} from '@nextui-org/react';

import formatDate from '@/utils/format-date';

import Circle from './Circle';
import Priority from './Priority';

export interface TodoInt {
  id: string;
  completed: boolean;
  priority: 'low' | 'neutral' | 'high' | 'critical';
  title: string;
  description?: string;
  date: Date;
}

export default function Todo({
  id,
  completed,
  priority,
  title,
  description,
  date,
}: TodoInt) {
  const [isCompleted, setIsCompleted] = useState(completed);

  const changeStatus = () => {
    setIsCompleted(!isCompleted);
    // edit with an api call on backend too
  };

  return (
    <Card className="bg-white/40 text-foreground-800 dark:bg-white/20">
      <CardBody className="flex flex-row items-center gap-2">
        <div className="ml-1 flex items-center gap-2">
          <Priority priority={priority} />
          <Button
            isIconOnly
            className="bg-transparent"
            onClick={changeStatus}
            disableRipple
          >
            {isCompleted ? (
              <CheckCircleIcon width={24} />
            ) : (
              <Circle width={24} />
            )}
          </Button>
          <p>{title}</p>
        </div>
        <div className="ml-auto flex items-center gap-2">
          <p className="text-sm">{formatDate(date)}</p>
          <Dropdown>
            <DropdownTrigger>
              <Button isIconOnly className="bg-transparent" disableRipple>
                <EllipsisVerticalIcon width={20} />
              </Button>
            </DropdownTrigger>
            <DropdownMenu aria-label="Todo Actions">
              <DropdownItem key="details">Show details</DropdownItem>
              <DropdownItem key="edit">Edit</DropdownItem>
              <DropdownItem key="delete" className="text-danger" color="danger">
                Delete
              </DropdownItem>
            </DropdownMenu>
          </Dropdown>
        </div>
      </CardBody>
    </Card>
  );
}
