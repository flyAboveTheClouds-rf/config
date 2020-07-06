set nocompatible

set number

syntax on

" smart-case-insensitivity
set smartcase

set hlsearch

set tabstop=4

set incsearch

set shiftwidth=4

set showmatch

set clipboard=unnamed

set autoindent

map <F8> <Esc>=%<Esc>

abbreviate ab abbreviate

abbreviate hed #include<stdio.h> int main() {  }

abbreviate #b /*********

abbreviate #e *********/

abbreviate im I'm

abbreviate al alias

nnoremap <silent> b[ :bprevious<CR>

nnoremap <silent> b] :bnext<CR>

nnoremap <silent> B[ :bfirst

nnoremap <silent> B] :blast
