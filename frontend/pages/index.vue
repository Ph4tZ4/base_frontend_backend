<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
    <!-- Hero Section -->
    <section class="relative overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-16">
        <div class="text-center">
          <h1 class="text-5xl md:text-7xl font-bold text-gray-900 mb-6">
            สร้างสรรค์สิ่ง
            <span class="bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 bg-clip-text text-transparent">
              อัศจรรย์
            </span>
          </h1>
          <p class="text-xl md:text-2xl text-gray-600 mb-8 max-w-3xl mx-auto leading-relaxed">
            สร้างแอปพลิเคชันเว็บที่สวยงามด้วยพลังของ Nuxt 3 และ TailwindCSS 
            เร็ว ตอบสนอง และสวยงามตั้งแต่เริ่มต้น
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl text-lg font-semibold transition-all transform hover:scale-105 shadow-lg hover:shadow-xl">
              เริ่มสร้าง
            </button>
            <button class="border-2 border-gray-300 hover:border-blue-600 text-gray-700 hover:text-blue-600 px-8 py-4 rounded-xl text-lg font-semibold transition-all transform hover:scale-105">
              เรียนรู้เพิ่มเติม
            </button>
          </div>
        </div>
      </div>
      
      <!-- Floating Elements -->
      <div class="absolute top-20 left-10 w-20 h-20 bg-blue-400/20 rounded-full blur-xl"></div>
      <div class="absolute top-40 right-20 w-32 h-32 bg-purple-400/20 rounded-full blur-xl"></div>
      <div class="absolute bottom-20 left-1/4 w-16 h-16 bg-indigo-400/20 rounded-full blur-xl"></div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-20 bg-white/50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold text-gray-900 mb-4">ทำไมต้องเลือกเรา</h2>
          <p class="text-xl text-gray-600 max-w-2xl mx-auto">
            คุณสมบัติที่ทรงพลังที่ทำให้การพัฒนาเร็วขึ้นและสนุกมากขึ้น
          </p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-2">
            <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mb-6">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">เร็วเหมือนสายฟ้า</h3>
            <p class="text-gray-600 leading-relaxed">
              สร้างขึ้นโดยคำนึงถึงประสิทธิภาพ แอปพลิเคชันของคุณจะโหลดเร็วและทำงานได้อย่างราบรื่นบนอุปกรณ์ใดก็ได้
            </p>
          </div>

          <!-- Feature 2 -->
          <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-2">
            <div class="w-12 h-12 bg-gradient-to-r from-purple-500 to-purple-600 rounded-xl flex items-center justify-center mb-6">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">การออกแบบที่ตอบสนอง</h3>
            <p class="text-gray-600 leading-relaxed">
              สวยงามและใช้งานได้บนทุกขนาดหน้าจอ TailwindCSS ทำให้การออกแบบที่ตอบสนองเป็นเรื่องง่าย
            </p>
          </div>

          <!-- Feature 3 -->
          <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-2">
            <div class="w-12 h-12 bg-gradient-to-r from-indigo-500 to-indigo-600 rounded-xl flex items-center justify-center mb-6">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">ประสบการณ์นักพัฒนา</h3>
            <p class="text-gray-600 leading-relaxed">
              เครื่องมือและเอกสารที่ยอดเยี่ยม มุ่งเน้นการสร้างคุณสมบัติ ไม่ใช่การตั้งค่า
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="py-20 bg-gradient-to-r from-blue-600 to-indigo-700">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid md:grid-cols-4 gap-8 text-center">
          <div>
            <div class="text-4xl font-bold text-white mb-2">10K+</div>
            <div class="text-blue-100">นักพัฒนาที่มีความสุข</div>
          </div>
          <div>
            <div class="text-4xl font-bold text-white mb-2">500+</div>
            <div class="text-blue-100">โปรเจกต์ที่สร้างขึ้น</div>
          </div>
          <div>
            <div class="text-4xl font-bold text-white mb-2">99.9%</div>
            <div class="text-blue-100">เวลาทำงาน</div>
          </div>
          <div>
            <div class="text-4xl font-bold text-white mb-2">24/7</div>
            <div class="text-blue-100">การสนับสนุน</div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-4xl font-bold text-gray-900 mb-6">พร้อมที่จะเริ่มต้นแล้วหรือยัง?</h2>
        <p class="text-xl text-gray-600 mb-8">
          เข้าร่วมกับนักพัฒนาหลายพันคนที่สร้างแอปพลิเคชันที่น่าทึ่งด้วยสแต็กของเรา
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <button class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl text-lg font-semibold transition-all transform hover:scale-105 shadow-lg">
            เริ่มโปรเจกต์ของคุณ
          </button>
          <button class="border-2 border-gray-300 hover:border-blue-600 text-gray-700 hover:text-blue-600 px-8 py-4 rounded-xl text-lg font-semibold transition-all">
            ดูเอกสาร
          </button>
        </div>
      </div>
    </section>
  </div>
</template>
