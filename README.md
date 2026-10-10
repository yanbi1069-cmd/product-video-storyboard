# Product Video Storyboard — Codex & Claude

Bộ skill v1, 10/10/2026. Chuyển **kịch bản đã duyệt + link/ảnh sản phẩm** thành prompt video FULL một đoạn tiếng Anh và storyboard ảnh dọc 6 ô. Không tự render video, không tự đăng bài, không tự scrape IG.

## Gói chia sẻ

Thư mục `product-video-storyboard/` là skill dùng chung, chứa SKILL.md, hướng dẫn tạo ảnh/prompt, checklist và script kiểm tra. Đây là phần có thể đưa lên GitHub sau khi duyệt. Không kèm token, ảnh khách hàng, lịch sử chat hoặc ảnh tham khảo của bên thứ ba. Chưa chọn giấy phép phân phối; quyết định license trước khi công khai.

Profile lưu file riêng của người dùng không đi kèm repository này. Hãy cung cấp quy ước đầu ra trong phiên/Project Instructions. Không phải plugin cung cấp sẵn image model: môi trường chạy cần có công cụ xem ảnh và tạo ảnh từ tham chiếu. Nếu thiếu, skill chỉ xuất đặc tả ảnh và phải báo chưa có PNG.

## Codex terminal

Copy toàn bộ thư mục `product-video-storyboard` vào `.agents/skills/` của dự án muốn dùng. Bắt đầu phiên từ dự án đó, kiểm tra skill được nhận và gọi `$product-video-storyboard`. Không chỉ copy SKILL.md, vì còn các reference/script. Bản bàn giao này chưa tự cài vào máy.

Tài liệu chính thức: https://developers.openai.com/codex/skills/

## Claude Code

Copy cùng thư mục vào `.claude/skills/` của dự án. Gọi `/product-video-storyboard`. Không có image tool thì không thể tạo storyboard PNG thật chỉ bằng việc cài skill.

Tài liệu: https://code.claude.com/docs/en/skills

## Claude web / Desktop

Custom Skills hiện yêu cầu ZIP chứa thư mục skill có SKILL.md, nhập trong Customize > Skills nếu tài khoản có tính năng. Gói này KHÔNG tự nén theo quy ước người dùng; chỉ tạo ZIP khi người dùng yêu cầu. GitHub URL không tự cài skill cho tài khoản Claude.

Nếu dùng Claude Project: đưa các file Markdown/TXT trong skill vào Project Knowledge, dùng `references/claude-project.md` làm Project Instructions. Đây là cách dùng hướng dẫn, không phải cài native skill và không bổ sung khả năng tạo ảnh.

Tài liệu: https://support.claude.com/en/articles/12512180-use-skills-in-claude

## Gửi đầu vào

```text
Dùng product-video-storyboard.
Sản phẩm: [link hoặc ảnh đính kèm]
Kịch bản: [diễn biến đã duyệt]
Thời lượng: 10 giây (hoặc thời lượng khác)
Âm thanh/chữ: [nếu đã có yêu cầu]
Đầu ra: prompt + SB (hoặc bộ đầy đủ có ảnh cảnh riêng)
Quy ước lưu: [đường dẫn/quy ước của bạn]
```

Chỉ sản phẩm + kịch bản là đầu vào bắt buộc; không hỏi lại những thông tin đã rõ. Thiếu ảnh xem được phải xin ảnh, không đoán sản phẩm. Thiếu CTA không tự sáng tác CTA.

## Kiểm tra

`python product-video-storyboard/scripts/check.py skill product-video-storyboard`

`python product-video-storyboard/scripts/check.py output [thư_mục_chứa_prompt.txt]`

Lệnh output chỉ kiểm tra file/một dòng/placeholder và kích thước PNG cơ bản, KHÔNG chứng minh đúng sản phẩm, đúng 6 ô hay video chạy thành công. Khi chưa có image tool, thêm `--text-only` để kiểm tra prompt.txt + img.txt thay PNG.

## GitHub

Chỉ publish phần đã duyệt sau khi chốt repository, public/private và quyền truy cập. Không tự tạo repo/push/install. `.gitignore` chỉ là lớp phòng ngừa; kiểm tra danh sách file thật trước mỗi lần upload. Nên lấy riêng thư mục gói này, không add cả thư mục IG.
