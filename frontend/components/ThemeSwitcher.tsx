'use client';

import { useEffect, useState } from 'react';
import { MoonIcon, SunIcon, WrenchIcon } from '@heroicons/react/24/outline';
import {
  Button,
  Dropdown,
  DropdownItem,
  DropdownMenu,
  DropdownTrigger,
} from '@nextui-org/react';
import { useTheme } from 'next-themes';

export default function ThemeSwitcher() {
  const [mounted, setMounted] = useState(false);
  const { theme, setTheme, systemTheme } = useTheme();

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  const currentTheme = theme === 'system' ? systemTheme : theme;

  const getNextTheme = () => {
    if (theme === 'light') return 'dark';
    if (theme === 'dark') return 'system';
    return 'light';
  };

  const thumbIcon = () => {
    if (currentTheme === 'light') return <SunIcon width={24} />;
    if (currentTheme === 'dark') return <MoonIcon width={24} />;
    return <WrenchIcon width={24} />;
  };

  return (
    <Dropdown>
      <DropdownTrigger>
        <Button isIconOnly className="bg-transparent shadow-lg">
          {thumbIcon()}
        </Button>
      </DropdownTrigger>
      <DropdownMenu
        aria-label="Theme Actions"
        onAction={(key) => setTheme(key as string)}
      >
        <DropdownItem key="light">Light mode</DropdownItem>
        <DropdownItem key="dark">Dark Mode</DropdownItem>
        <DropdownItem key="system">Use system setting</DropdownItem>
      </DropdownMenu>
    </Dropdown>
  );
}
