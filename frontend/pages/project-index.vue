<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
    <!-- Project Overview Section -->
    <section class="py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h1 class="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
            เทมเพลต
            <span class="bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 bg-clip-text text-transparent">
              โปรเจกต์
            </span>
          </h1>
          <p class="text-xl md:text-2xl text-gray-600 mb-8 max-w-3xl mx-auto">
            เทมเพลต Frontend-Backend พื้นฐานด้วย Nuxt 3 + Flask + TailwindCSS
          </p>
          <div class="flex flex-wrap justify-center gap-4 mb-8">
            <span class="bg-blue-100 text-blue-800 px-4 py-2 rounded-full text-sm font-semibold">Nuxt 3</span>
            <span class="bg-green-100 text-green-800 px-4 py-2 rounded-full text-sm font-semibold">Vue 3</span>
            <span class="bg-purple-100 text-purple-800 px-4 py-2 rounded-full text-sm font-semibold">TailwindCSS</span>
            <span class="bg-yellow-100 text-yellow-800 px-4 py-2 rounded-full text-sm font-semibold">Flask</span>
            <span class="bg-red-100 text-red-800 px-4 py-2 rounded-full text-sm font-semibold">Python</span>
            <span class="bg-indigo-100 text-indigo-800 px-4 py-2 rounded-full text-sm font-semibold">TypeScript</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Available Features Grid -->
    <section class="py-20 bg-white/50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold text-gray-900 mb-4">คุณสมบัติที่มีให้</h2>
          <p class="text-xl text-gray-600 max-w-2xl mx-auto">
            ทุกอย่างที่คุณต้องการเพื่อสร้างแอปพลิเคชันเว็บสมัยใหม่
          </p>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Frontend Features -->
          <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-2 border-l-4 border-blue-500">
            <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mb-6">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Frontend (Nuxt 3)</h3>
            <ul class="space-y-2 text-gray-600">
              <li class="flex items-center"><span class="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>Vue 3 Composition API</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>รองรับ TypeScript</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>การจัดรูปแบบด้วย TailwindCSS</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>สถาปัตยกรรมคอมโพเนนต์</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>ระบบเลย์เอาต์</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>การแทนที่โมดูลแบบร้อน</li>
            </ul>
          </div>

          <!-- Backend Features -->
          <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-2 border-l-4 border-green-500">
            <div class="w-12 h-12 bg-gradient-to-r from-green-500 to-green-600 rounded-xl flex items-center justify-center mb-6">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Backend (Flask)</h3>
            <ul class="space-y-2 text-gray-600">
              <li class="flex items-center"><span class="w-2 h-2 bg-green-500 rounded-full mr-3"></span>RESTful API</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-green-500 rounded-full mr-3"></span>ระบบการยืนยันตัวตน</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-green-500 rounded-full mr-3"></span>โมเดลฐานข้อมูล</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-green-500 rounded-full mr-3"></span>การจัดระเบียบเส้นทาง</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-green-500 rounded-full mr-3"></span>การจัดการการตั้งค่า</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-green-500 rounded-full mr-3"></span>รองรับ CORS</li>
            </ul>
          </div>

          <!-- Design Features -->
          <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-2 border-l-4 border-purple-500">
            <div class="w-12 h-12 bg-gradient-to-r from-purple-500 to-purple-600 rounded-xl flex items-center justify-center mb-6">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zM21 5a2 2 0 00-2-2h-4a2 2 0 00-2 2v12a4 4 0 004 4h4a2 2 0 002-2V5z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">ระบบการออกแบบ</h3>
            <ul class="space-y-2 text-gray-600">
              <li class="flex items-center"><span class="w-2 h-2 bg-purple-500 rounded-full mr-3"></span>การออกแบบที่ตอบสนอง</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-purple-500 rounded-full mr-3"></span>คอมโพเนนต์ UI สมัยใหม่</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-purple-500 rounded-full mr-3"></span>เอฟเฟกต์ไล่ระดับ</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-purple-500 rounded-full mr-3"></span>แอนิเมชันเมื่อวางเมาส์</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-purple-500 rounded-full mr-3"></span>แนวทาง Mobile-First</li>
              <li class="flex items-center"><span class="w-2 h-2 bg-purple-500 rounded-full mr-3"></span>พร้อมสำหรับการเข้าถึง</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- File Structure Section -->
    <section class="py-20 bg-gray-900 text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold mb-4">โครงสร้างโปรเจกต์</h2>
          <p class="text-xl text-gray-300 max-w-2xl mx-auto">
            โครงสร้างไฟล์ที่จัดระเบียบสำหรับการพัฒนาที่ขยายได้
          </p>
        </div>
        
        <div class="grid md:grid-cols-2 gap-8">
          <!-- Frontend Structure -->
          <div class="bg-gray-800 rounded-2xl p-8">
            <h3 class="text-2xl font-semibold mb-6 text-blue-400">โครงสร้าง Frontend</h3>
            <div class="space-y-3 text-sm font-mono">
              <div class="flex items-center">
                <span class="text-green-400 mr-2">📁</span>
                <span class="text-gray-300">frontend/</span>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-blue-400 mr-2">📁</span>
                <span class="text-gray-300">components/</span>
              </div>
              <div class="flex items-center ml-8">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">Header.vue</span>
              </div>
              <div class="flex items-center ml-8">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">Footer.vue</span>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-blue-400 mr-2">📁</span>
                <span class="text-gray-300">layouts/</span>
              </div>
              <div class="flex items-center ml-8">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">default.vue</span>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-blue-400 mr-2">📁</span>
                <span class="text-gray-300">pages/</span>
              </div>
              <div class="flex items-center ml-8">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">index.vue</span>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-blue-400 mr-2">📁</span>
                <span class="text-gray-300">assets/css/</span>
              </div>
              <div class="flex items-center ml-8">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">main.css</span>
              </div>
            </div>
          </div>

          <!-- Backend Structure -->
          <div class="bg-gray-800 rounded-2xl p-8">
            <h3 class="text-2xl font-semibold mb-6 text-green-400">โครงสร้าง Backend</h3>
            <div class="space-y-3 text-sm font-mono">
              <div class="flex items-center">
                <span class="text-green-400 mr-2">📁</span>
                <span class="text-gray-300">backend/</span>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-blue-400 mr-2">📁</span>
                <span class="text-gray-300">routes/</span>
              </div>
              <div class="flex items-center ml-8">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">auth.py</span>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">app.py</span>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">config.py</span>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">models.py</span>
              </div>
              <div class="flex items-center ml-4">
                <span class="text-yellow-400 mr-2">📄</span>
                <span class="text-gray-300">requirements.txt</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick Start Section -->
    <section class="py-20 bg-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-4xl font-bold text-gray-900 mb-6">คู่มือการเริ่มต้นอย่างรวดเร็ว</h2>
        <p class="text-xl text-gray-600 mb-8">
          ทำให้โปรเจกต์ของคุณทำงานได้ในไม่กี่นาที
        </p>
        
        <div class="grid md:grid-cols-2 gap-8 text-left">
          <!-- Frontend Setup -->
          <div class="bg-gray-50 rounded-xl p-6">
            <h3 class="text-xl font-semibold text-gray-900 mb-4">การตั้งค่า Frontend</h3>
            <div class="space-y-3">
              <div class="bg-gray-900 text-green-400 p-3 rounded-lg font-mono text-sm">
                <div>cd frontend</div>
                <div>npm install</div>
                <div>npm run dev</div>
              </div>
              <p class="text-gray-600 text-sm">
                Frontend จะพร้อมใช้งานที่: <span class="font-mono text-blue-600">http://localhost:3000</span>
              </p>
            </div>
          </div>

          <!-- Backend Setup -->
          <div class="bg-gray-50 rounded-xl p-6">
            <h3 class="text-xl font-semibold text-gray-900 mb-4">การตั้งค่า Backend</h3>
            <div class="space-y-3">
              <div class="bg-gray-900 text-green-400 p-3 rounded-lg font-mono text-sm">
                <div>cd backend</div>
                <div>pip install -r requirements.txt</div>
                <div>python app.py</div>
              </div>
              <p class="text-gray-600 text-sm">
                Backend API จะพร้อมใช้งานที่: <span class="font-mono text-blue-600">http://localhost:5000</span>
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Navigation Links -->
    <section class="py-20 bg-gradient-to-r from-blue-600 to-indigo-700">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-4xl font-bold text-white mb-6">พร้อมที่จะสำรวจแล้วหรือยัง?</h2>
        <p class="text-xl text-blue-100 mb-8">
          ดูหน้าต่างๆ และคุณสมบัติที่มีให้
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <NuxtLink to="/" class="bg-white hover:bg-gray-100 text-blue-600 px-8 py-4 rounded-xl text-lg font-semibold transition-all transform hover:scale-105 shadow-lg">
            ดูหน้าหลัก
          </NuxtLink>
          <a href="https://github.com" target="_blank" class="border-2 border-white text-white hover:bg-white hover:text-blue-600 px-8 py-4 rounded-xl text-lg font-semibold transition-all">
            ดูบน GitHub
          </a>
        </div>
      </div>
    </section>
  </div>
</template>
