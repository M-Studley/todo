import React from 'react';
import {
  CheckCircleIcon,
  EllipsisVerticalIcon,
} from '@heroicons/react/24/outline';
import { Card, CardBody } from '@nextui-org/react';

import Circle from './Circle';
import Priority from './Priority';

interface Todo {
  status: 'completed' | 'not completed';
  priority: 'low' | 'neutral' | 'high' | 'critical';
  title: string;
  description?: string;
  date: Date;
}

export default function Todo({
  status,
  priority,
  title,
  description,
  date,
}: Todo) {
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
          <EllipsisVerticalIcon width={20} />
        </div>
      </CardBody>
    </Card>
  );
}
