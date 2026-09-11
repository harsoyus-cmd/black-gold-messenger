import 'package:flutter/material.dart';

void main() {
  runApp(const BgmApp());
}

class BgmApp extends StatelessWidget {
  const BgmApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'BGM',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: Brightness.dark,
        fontFamily: 'Atkinson Hyperlegible',
        scaffoldBackgroundColor: const Color(0xFF050505),
        colorScheme: const ColorScheme.dark(
          primary: Color(0xFFD4AF37),
          surface: Color(0xFF0D0D0D),
          onSurface: Color(0xFFF5F5F5),
        ),
      ),
      home: const BgmHomeScreen(),
    );
  }
}

class BgmHomeScreen extends StatefulWidget {
  const BgmHomeScreen({super.key});

  @override
  State<BgmHomeScreen> createState() => _BgmHomeScreenState();
}

class _BgmHomeScreenState extends State<BgmHomeScreen> {
  int _selectedIndex = 0;

  static const _gold = Color(0xFFD4AF37);
  static const _surface = Color(0xFF0D0D0D);
  static const _textPrimary = Color(0xFFF5F5F5);
  static const _textSecondary = Color(0xFFB8B8B8);

  static const _destinations = <_BgmDestination>[
    _BgmDestination('Chat', Icons.chat_outlined),
    _BgmDestination('World', Icons.public_outlined),
    _BgmDestination('Radio', Icons.radio_outlined),
    _BgmDestination('Profile', Icons.person_outline),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.black,
        elevation: 0,
        centerTitle: false,
        titleSpacing: 20,
        title: const Text(
          'BGM',
          style: TextStyle(
            color: _textPrimary,
            fontSize: 22,
            fontWeight: FontWeight.w700,
            letterSpacing: 0.4,
          ),
        ),
      ),
      body: IndexedStack(
        index: _selectedIndex,
        children: const [
          _HomeContent(),
          _DestinationPage(title: 'World'),
          _DestinationPage(title: 'Radio'),
          _DestinationPage(title: 'Profile'),
        ],
      ),
      bottomNavigationBar: SafeArea(
        top: false,
        child: Container(
          decoration: const BoxDecoration(
            color: _surface,
            border: Border(
              top: BorderSide(
                color: Color(0xFF151515),
                width: 1,
              ),
            ),
          ),
          child: NavigationBar(
            height: 68,
            backgroundColor: _surface,
            elevation: 0,
            selectedIndex: _selectedIndex,
            onDestinationSelected: (index) {
              setState(() => _selectedIndex = index);
            },
            indicatorColor: Colors.transparent,
            labelBehavior: NavigationDestinationLabelBehavior.alwaysShow,
            destinations: _destinations.map((destination) {
              final index = _destinations.indexOf(destination);
              final active = index == _selectedIndex;

              return NavigationDestination(
                icon: Icon(
                  destination.icon,
                  size: 23,
                  color: active ? _gold : _textSecondary,
                ),
                selectedIcon: Icon(
                  destination.icon,
                  size: 23,
                  color: _gold,
                ),
                label: destination.label,
              );
            }).toList(),
          ),
        ),
      ),
    );
  }
}

class _HomeContent extends StatelessWidget {
  const _HomeContent();

  @override
  Widget build(BuildContext context) {
    return const Padding(
      padding: EdgeInsets.fromLTRB(20, 8, 20, 20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _IdentityHeader(),
          SizedBox(height: 28),
          Text(
            'Recent Conversations',
            style: TextStyle(
              color: _BgmHomeColors.textPrimary,
              fontSize: 18,
              fontWeight: FontWeight.w700,
            ),
          ),
          SizedBox(height: 18),
          Expanded(
            child: _EmptyConversationState(),
          ),
        ],
      ),
    );
  }
}

class _IdentityHeader extends StatelessWidget {
  const _IdentityHeader();

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Container(
          width: 48,
          height: 48,
          decoration: BoxDecoration(
            color: _BgmHomeColors.surface2,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(
              color: _BgmHomeColors.goldDark,
              width: 1,
            ),
          ),
          child: const Icon(
            Icons.person_outline,
            color: _BgmHomeColors.gold,
            size: 25,
          ),
        ),
        const SizedBox(width: 14),
        const Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'BGM Identity',
                style: TextStyle(
                  color: _BgmHomeColors.textPrimary,
                  fontSize: 16,
                  fontWeight: FontWeight.w700,
                ),
              ),
              SizedBox(height: 3),
              Text(
                'Your identity and conversations',
                style: TextStyle(
                  color: _BgmHomeColors.textSecondary,
                  fontSize: 13,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class _EmptyConversationState extends StatelessWidget {
  const _EmptyConversationState();

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: const [
          Icon(
            Icons.chat_bubble_outline,
            color: _BgmHomeColors.textMuted,
            size: 32,
          ),
          SizedBox(height: 12),
          Text(
            'No recent conversations',
            textAlign: TextAlign.center,
            style: TextStyle(
              color: _BgmHomeColors.textSecondary,
              fontSize: 15,
            ),
          ),
        ],
      ),
    );
  }
}

class _DestinationPage extends StatelessWidget {
  final String title;

  const _DestinationPage({required this.title});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text(
        title,
        style: const TextStyle(
          color: _BgmHomeColors.textPrimary,
          fontSize: 20,
          fontWeight: FontWeight.w700,
        ),
      ),
    );
  }
}

class _BgmDestination {
  final String label;
  final IconData icon;

  const _BgmDestination(this.label, this.icon);
}

class _BgmHomeColors {
  static const surface2 = Color(0xFF151515);
  static const gold = Color(0xFFD4AF37);
  static const goldDark = Color(0xFF9C7C19);
  static const textPrimary = Color(0xFFF5F5F5);
  static const textSecondary = Color(0xFFB8B8B8);
  static const textMuted = Color(0xFF777777);
}
