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
  useDisclosure,
} from '@nextui-org/react';

import formatDate from '@/utils/format-date';

import Circle from './Circle';
import Priority from './Priority';
import TodoDetails from './TodoDetails';

export interface TodoInt {
  id: string;
  completed: boolean;
  priority: 'low' | 'neutral' | 'high' | 'critical';
  title: string;
  description: string;
  dueDate: Date;
  createdAt: Date;
}

export default function Todo({
  id,
  completed,
  priority,
  title,
  description,
  dueDate: dueDate,
  createdAt: createdAt,
}: TodoInt) {
  const [isCompleted, setIsCompleted] = useState(completed);

  // nextui custom hook for modal
  const { isOpen, onOpen, onOpenChange } = useDisclosure();

  const changeStatus = () => {
    setIsCompleted(!isCompleted);
    // TODO edit with an api call on backend too
  };

  return (
    <>
      <Card className="bg-white/40 text-foreground-800 dark:bg-black/30">
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
            <p className="text-sm">{formatDate(dueDate)}</p>
            <Dropdown
              className="bg-white/30 backdrop-blur-lg dark:bg-black/30"
              disableAnimation
            >
              <DropdownTrigger>
                <Button isIconOnly className="bg-transparent" disableRipple>
                  <EllipsisVerticalIcon width={20} />
                </Button>
              </DropdownTrigger>
              <DropdownMenu aria-label="Todo Actions">
                <DropdownItem key="details" onPress={onOpen}>
                  Show details
                </DropdownItem>
                <DropdownItem key="edit">Edit</DropdownItem>
                <DropdownItem
                  key="delete"
                  className="text-danger"
                  color="danger"
                >
                  Delete
                </DropdownItem>
              </DropdownMenu>
            </Dropdown>
          </div>
        </CardBody>
      </Card>
      <TodoDetails
        isOpen={isOpen}
        onOpenChange={onOpenChange}
        description={description}
        createdAt={createdAt}
      />
    </>
  );
}
