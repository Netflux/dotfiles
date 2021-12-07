if empty(glob('~/.local/share/nvim/site/autoload/plug.vim'))
	silent !curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
	autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin('~/.local/share/nvim/plugged')

Plug 'qpkorr/vim-bufkill'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'cocopon/iceberg.vim'

call plug#end()

" Theme settings
colorscheme iceberg
let g:airline_theme = "minimalist"
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:enable_bold_font = 1

" General settings
set hidden
set number
set background=dark
set clipboard^=unnamedplus
set mouse=a
set updatetime=1000

" Tab settings
set noexpandtab
set tabstop=4
set shiftwidth=4

" Window settings
set splitright
set splitbelow

" NERDTree settings
let g:NERDTreeChDirMode = 2
let g:NERDTreeNaturalSort = 1
let g:NERDTreeMouseMode = 2
let g:NERDTreeShowIgnoredStatus = 1

" General keybinds
map <Space> <Leader>

" NERDTree keybinds
noremap <Leader>t :NERDTreeToggle<CR>
noremap <Leader>r :NERDTreeFind<CR>
noremap <Leader><S-r> :NERDTreeFocus<CR>:execute "normal R"<CR>:wincmd p<CR>

" Delete to black hole register
nnoremap d "_d
nnoremap D "_D
vnoremap d "_d

" Buffer management
nnoremap gb :ls<CR>:b<Space>
nnoremap <Tab> :bnext<CR>:ls<CR>
nnoremap <S-Tab> :bprevious<CR>:ls<CR>

" Window management
function! WinMove(key)
	let t:curwin = winnr()
	exec "wincmd ".a:key
	if (t:curwin == winnr())
		if (match(a:key, '[jk]'))
			wincmd v
		else
			wincmd s
		endif
		exec "wincmd ".a:key
	endif
endfunction

noremap <Leader>h :call WinMove('h')<CR>
noremap <Leader>j :call WinMove('j')<CR>
noremap <Leader>k :call WinMove('k')<CR>
noremap <Leader>l :call WinMove('l')<CR>

" Autocommands
augroup default
	autocmd!

	" Reload buffer if modified externally
	autocmd BufEnter,CursorHold,CursorHoldI,CursorMoved,CursorMovedI * checktime
	autocmd FileChangedShellPost * echohl WarningMsg | echo "Buffer changed!" | echohl None
	
	" Open NERDTree if editing a directory
	autocmd StdinReadPre * let s:std_in=1
	autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif

	" Close NERDTree if no other windows exist
	autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
augroup END
