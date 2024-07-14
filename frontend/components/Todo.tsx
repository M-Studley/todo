'use client';
import React from 'react';
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

import Circle from './Circle';
import Priority from './Priority';

export interface TodoInt {
  id: string;
  status: 'completed' | 'not completed';
  priority: 'low' | 'neutral' | 'high' | 'critical';
  title: string;
  description?: string;
  date: Date;
}

export default function Todo({
  id,
  status,
  priority,
  title,
  description,
  date,
}: TodoInt) {
  const formattedDate = new Intl.DateTimeFormat('en-US', {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(date);

  return (
    <Card className="bg-white/40 text-foreground-800 dark:bg-white/20">
      <CardBody className="flex flex-row items-center gap-2">
        <div className="ml-1 flex items-center gap-2">
          <Priority priority={priority} />
          {status === 'completed' ? (
            <CheckCircleIcon width={24} />
          ) : (
            <Circle width={22} />
          )}
          <p>{title}</p>
        </div>
        <div className="ml-auto flex items-center gap-2">
          <p className="text-sm">{formattedDate}</p>
          <Dropdown>
            <DropdownTrigger>
              <Button isIconOnly className="w-4 bg-transparent">
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
