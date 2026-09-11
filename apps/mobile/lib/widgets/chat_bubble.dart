import 'package:flutter/material.dart';

class ChatBubble extends StatefulWidget {
  final String sender;
  final String originalText;
  final bool isMe;
  final String sourceLang;
  final String targetLang;

  const ChatBubble({
    Key? key,
    required this.sender,
    required this.originalText,
    required this.isMe,
    this.sourceLang = 'en',
    this.targetLang = 'id',
  }) : super(key: key);

  @override
  _ChatBubbleState createState() => _ChatBubbleState();
}

class _ChatBubbleState extends State<ChatBubble> {
  bool _isTranslated = false;
  bool _isLoading = false;
  String _translatedText = "";

  // Fungsi ini nantinya akan memanggil core Python (BGMTranslationService) secara lokal
  void _translateMessage() async {
    setState(() {
      _isLoading = true;
    });

    // Simulasi delay pemrosesan AI lokal (Edge AI) selama 1 detik
    await Future.delayed(const Duration(seconds: 1));

    setState(() {
      // Simulasi hasil terjemahan dari backend P2P lokal kita
      _translatedText = "[${widget.targetLang.toUpperCase()} - P2P Lokal] ${widget.originalText}";
      _isTranslated = true;
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: widget.isMe ? Alignment.centerRight : Alignment.centerLeft,
      child: Container(
        margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 16),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: widget.isMe ? Colors.blueGrey[800] : Colors.grey[850],
          borderRadius: BorderRadius.circular(16).copyWith(
            bottomRight: widget.isMe ? const Radius.circular(0) : const Radius.circular(16),
            bottomLeft: !widget.isMe ? const Radius.circular(0) : const Radius.circular(16),
          ),
          boxShadow: [
            BoxShadow(color: Colors.black26, blurRadius: 4, offset: Offset(0, 2))
          ],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            // Nama Pengirim
            Text(
              widget.sender,
              style: TextStyle(
                color: widget.isMe ? Colors.amber[400] : Colors.greenAccent,
                fontWeight: FontWeight.bold,
                fontSize: 12,
              ),
            ),
            const SizedBox(height: 6),
            
            // Teks Asli
            Text(
              widget.originalText,
              style: const TextStyle(color: Colors.white, fontSize: 16),
            ),
            
            // Tombol Terjemahan atau Hasil Terjemahan
            if (!_isTranslated && !widget.isMe) ...[
              const SizedBox(height: 8),
              _isLoading 
                ? const SizedBox(
                    height: 20, 
                    width: 20, 
                    child: CircularProgressIndicator(strokeWidth: 2, color: Colors.amber)
                  )
                : InkWell(
                    onTap: _translateMessage,
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.translate, size: 16, color: Colors.amber[200]),
                        const SizedBox(width: 4),
                        Text(
                          "Terjemahkan",
                          style: TextStyle(color: Colors.amber[200], fontSize: 12),
                        ),
                      ],
                    ),
                  ),
            ] else if (_isTranslated) ...[
              const Padding(
                padding: EdgeInsets.symmetric(vertical: 6.0),
                child: Divider(color: Colors.white30, height: 1),
              ),
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Icon(Icons.g_translate, size: 14, color: Colors.amber),
                  const SizedBox(width: 6),
                  Expanded(
                    child: Text(
                      _translatedText,
                      style: const TextStyle(
                        color: Colors.amber, 
                        fontSize: 15, 
                        fontStyle: FontStyle.italic
                      ),
                    ),
                  ),
                ],
              )
            ]
          ],
        ),
      ),
    );
  }
}
