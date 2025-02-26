result = nvim.call
`nvim_`, e.g. `nvim_list_bufs`.
nvim_error_event[{type}, {message}]
nvim_buf_lines_event[{buf}, {changedtick}, {firstline}, {lastline}, {linedata}, {more}]
nvim_buf_changedtick_event[{buf}, {changedtick}]   nvim_buf_detach_event[{buf}]                            nvim_buf_lines_event[{buf}, {changedtick}, 0, -1, [""], v:false]
nvim_buf_lines_event[{buf}, {changedtick}, 0, 0, ["line1", "line2"], v:false]
nvim_buf_lines_event[{buf}, {changedtick}, {linenr}, {linenr} + 1,
nvim_buf_lines_event[{buf}, {changedtick}, 2, 22, [], v:false]
nvim_buf_lines_event[{buf}, {changedtick}, 2, 5,
nvim_buf_detach_event[{buf}]
vim.api.nvim_buf_get_lines
vim.api.nvim_buf_add_highlight
extid = vim.api.nvim_buf_set_extmark
vim.api.nvim_buf_set_extmark
vim.api.nvim_buf_set_extmark
call nvim_buf_set_lines
let src = nvim_buf_add_highlight
call nvim_buf_add_highlight
call nvim_buf_clear_namespace
if vim.api.nvim_win_get_config
let buf = nvim_create_buf
call nvim_buf_set_lines
let win = nvim_open_win
call nvim_set_option_value
let g:mark_ns = nvim_create_namespace
let g:mark_id = nvim_buf_set_extmark
echo nvim_buf_get_extmark_by_id
echo nvim_buf_get_extmarks
echo nvim_buf_get_extmark_by_id
nvim_chan_send
nvim_create_buf
nvim_del_current_line
nvim_del_keymap
nvim_del_mark
nvim_del_var
nvim_echo
nvim_err_write
nvim_err_writeln
• nvim_err_write
nvim_eval_statusline
nvim_exec_lua
nvim_feedkeys
nvim_feedkeys
:let key = nvim_replace_termcodes
:call nvim_feedkeys
nvim_get_api_info
nvim_get_chan_info
nvim_get_color_by_name
:echo nvim_get_color_by_name
:echo nvim_get_color_by_name
nvim_get_color_map
nvim_get_context
nvim_get_current_buf
nvim_get_current_line
nvim_get_current_tabpage
nvim_get_current_win
nvim_get_hl
nvim_get_hl_id_by_name
nvim_get_hl_ns
nvim_get_keymap
nvim_get_mark
nvim_get_mode
nvim_get_proc
nvim_get_proc_children
nvim_get_runtime_file
nvim_get_runtime_file
nvim_get_var
nvim_get_vvar
nvim_input
nvim_input_mouse
nvim_list_bufs
nvim_list_chans
nvim_list_runtime_paths
nvim_list_tabpages
nvim_list_uis
nvim_list_wins
nvim_load_context
nvim_notify
nvim_open_term
nvim_out_write
nvim_paste
"stream" a paste, call `nvim_paste` sequentially with these
nvim_put
nvim_replace_termcodes
nvim_select_popupmenu_item
nvim_set_client_info
nvim_set_current_buf
nvim_set_current_dir
nvim_set_current_line
nvim_set_current_tabpage
nvim_set_current_win
nvim_set_hl
`nvim_set_hl
nvim_set_hl_ns
nvim_set_hl_ns_fast
nvim_set_keymap
call nvim_set_keymap
nvim_set_var
nvim_set_vvar
nvim_strwidth
nvim__complete_set
nvim__get_runtime
nvim__id
nvim__id_array
nvim__id_dictionary
nvim__id_float
nvim__inspect_cell
nvim__invalidate_glyph_cache
nvim__redraw
nvim__stats
nvim_call_dict_function
nvim_call_function
nvim_command
nvim_eval
nvim_exec2
nvim_parse_expression
nvim_buf_create_user_command
• nvim_create_user_command
nvim_buf_del_user_command
nvim_buf_get_commands
nvim_cmd
nvim_create_user_command
:call nvim_create_user_command
nvim_del_user_command
nvim_get_commands
nvim_parse_cmd
nvim_get_all_options_info
nvim_get_option_info2
nvim_get_option_value
nvim_set_option_value
nvim_buf_attach
vim.api.nvim_buf_attach
`nvim_buf_lines_event`. Else the first notification
will be `nvim_buf_changedtick_event`. Not for Lua
nvim_buf_call
nvim_buf_del_keymap
nvim_buf_del_mark
nvim_buf_del_var
nvim_buf_delete
nvim_buf_detach
nvim_buf_get_changedtick
nvim_buf_get_keymap
nvim_buf_get_lines
nvim_buf_get_mark
nvim_buf_get_name
nvim_buf_get_offset
nvim_buf_get_text
nvim_buf_get_var
nvim_buf_is_loaded
nvim_buf_is_valid
nvim_buf_line_count
nvim_buf_set_keymap
nvim_buf_set_lines
nvim_buf_set_mark
nvim_buf_set_name
nvim_buf_set_text
nvim_buf_set_var
nvim_buf_add_highlight
nvim_buf_clear_namespace
nvim_buf_del_extmark
nvim_buf_get_extmark_by_id
nvim_buf_get_extmarks
vim.api.nvim_buf_get_extmarks
vim.api.nvim_buf_get_extmarks
local pos = api.nvim_win_get_cursor
local ns  = api.nvim_create_namespace
local m1  = api.nvim_buf_set_extmark
local m2  = api.nvim_buf_set_extmark
local ms  = api.nvim_buf_get_extmarks
local all = api.nvim_buf_get_extmarks
nvim_buf_set_extmark
nvim_create_namespace
nvim_get_namespaces
nvim_set_decoration_provider
nvim__win_add_ns
nvim__win_del_ns
nvim__win_get_ns
nvim_win_call
nvim_win_close
nvim_win_del_var
nvim_win_get_buf
nvim_win_get_cursor
nvim_win_get_height
nvim_win_get_number
nvim_win_get_position
nvim_win_get_tabpage
nvim_win_get_var
nvim_win_get_width
nvim_win_hide
nvim_win_is_valid
nvim_win_set_buf
nvim_win_set_cursor
nvim_win_set_height
nvim_win_set_hl_ns
nvim_win_set_var
nvim_win_set_width
nvim_win_text_height
nvim_open_win
vim.api.nvim_open_win
vim.api.nvim_open_win
vim.api.nvim_open_win
nvim_win_get_config
nvim_win_set_config
nvim_tabpage_del_var
nvim_tabpage_get_number
nvim_tabpage_get_var
nvim_tabpage_get_win
nvim_tabpage_is_valid
nvim_tabpage_list_wins
nvim_tabpage_set_var
nvim_tabpage_set_win
nvim_clear_autocmds
nvim_create_augroup
local id = vim.api.nvim_create_augroup
nvim_create_autocmd
vim.api.nvim_create_autocmd
vim.api.nvim_create_autocmd
nvim_del_augroup_by_id
nvim_del_augroup_by_name
nvim_del_autocmd
nvim_exec_autocmds
nvim_get_autocmds
autocommands = vim.api.nvim_get_autocmds
autocommands = vim.api.nvim_get_autocmds
nvim_ui_attach
nvim_ui_detach
nvim_ui_pum_set_bounds
nvim_ui_pum_set_height
nvim_ui_set_focus
nvim_ui_set_option
nvim_ui_term_event
nvim_ui_try_resize
nvim_ui_try_resize_grid
