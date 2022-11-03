
class _AccountantState extends State<Accountant> {
  late NodesDatabase nodeDB;
  late List<Node> NODES;
  bool isLoading = false;

  @override
  void initState() {
    super.initState();

    nodeDB = NodesDatabase.instance;

    refreshNodes();
  }

  Future refreshNodes() async {
    setState(() => isLoading = true);

    NODES = await NodesDatabase.instance.readAllNodes();

    setState(() => isLoading = false);
  }

  @override
  Widget build(BuildContext context) {
    // DB Interaction

    var nodeDB = NodesDatabase.instance;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Accountant'),
        backgroundColor: Colors.black54,
        actions: [
          IconButton(onPressed: createNode, icon: const Icon(Icons.add))
        ],
      ),
      body: isLoading
          ? const Center(child: CircularProgressIndicator())
          : WIDGET(NODES: NODES),
    );
  }
}
