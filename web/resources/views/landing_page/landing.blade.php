@extends('layouts.app')

@section('title', 'Landing Page')

@push('styles')
<link rel="stylesheet" href="{{ asset('css/style.css') }}">
@endpush

@section('content')

    <div class="navbar">
        <div class="container">
            <img src="{{ asset('img/logo-lensa.png') }}" class="logo-img">

            <a href="{{ route('login') }}" class="btn-login">
                <iconify-icon icon="mdi:user" width="20"></iconify-icon>
                Daftar | Masuk
            </a>
        </div>
    </div>

    {{-- HERO --}}
    @include('landing_page.sections.hero')

    {{-- FEATURES --}}
    @include('landing_page.sections.top-features')

    {{-- FITUR --}}
    @include('landing_page.sections.fitur')

    {{-- HOW --}}
    @include('landing_page.sections.how')

    <footer>
        lensa_hoax@2026
    </footer>

    @endsection
