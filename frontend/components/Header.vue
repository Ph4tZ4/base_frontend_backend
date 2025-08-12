<template>
  <nav class="bg-white/80 backdrop-blur-md border-b border-gray-200/50 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <div class="flex items-center space-x-2">
          <div class="w-8 h-8 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center">
            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <span class="text-xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
            NuxtApp
          </span>
        </div>
        <div class="hidden md:flex items-center space-x-8">
          <NuxtLink to="/" class="text-gray-600 hover:text-blue-600 transition-colors">หน้าแรก</NuxtLink>
          <NuxtLink to="/project-index" class="text-gray-600 hover:text-blue-600 transition-colors">ดัชนีโปรเจกต์</NuxtLink>
          <a href="#features" class="text-gray-600 hover:text-blue-600 transition-colors">คุณสมบัติ</a>
          <a href="#about" class="text-gray-600 hover:text-blue-600 transition-colors">เกี่ยวกับ</a>
          <a href="#contact" class="text-gray-600 hover:text-blue-600 transition-colors">ติดต่อ</a>
          <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors">
            เริ่มต้น
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>
