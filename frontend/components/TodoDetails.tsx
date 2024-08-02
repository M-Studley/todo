'use client';
import React from 'react';
import {
  Button,
  Divider,
  Modal,
  ModalBody,
  ModalContent,
  ModalFooter,
  ModalHeader,
} from '@nextui-org/react';

import Priority from '@/components/Priority';

export default function TodoDetails({
  isOpen,
  onOpenChange,
  name,
  description,
  createdAt,
  deadline,
  category,
  priority,
}: {
  isOpen: boolean;
  onOpenChange: () => void;
  name: string;
  description?: string;
  createdAt: Date;
  deadline?: Date;
  category: string;
  priority: 'low' | 'neutral' | 'high' | 'critical';
}) {
  return (
    <>
      <Modal
        isOpen={isOpen}
        onOpenChange={onOpenChange}
        className="bg-white/40 dark:bg-black/50"
        backdrop="blur"
        size="xl"
      >
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex gap-2">
                <Priority priority={priority} />
                {name}
              </ModalHeader>
              <ModalBody>
                <div className="flex">
                  <p className="self-end text-sm">{category}</p>
                  <div className="ml-auto flex flex-col text-right">
                    <p className="text-sm">
                      Added: {createdAt.toLocaleDateString()}
                    </p>
                    {deadline && (
                      <p
                        className={`text-sm ${deadline < new Date() && 'text-danger-500'}`}
                      >
                        Deadline: {deadline.toLocaleDateString()}
                      </p>
                    )}
                  </div>
                </div>
                <Divider />
                {description && (
                  <div className="max-h-32 overflow-y-auto">{description}</div>
                )}
              </ModalBody>
              <ModalFooter>
                <Button color="primary" onPress={onClose}>
                  Ok
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>
    </>
  );
}
