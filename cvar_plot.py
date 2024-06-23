{"metadata":{"colab":{"provenance":[]},"kaggle":{"accelerator":"nvidiaTeslaT4","dataSources":[{"sourceId":4988910,"sourceType":"datasetVersion","datasetId":2893580},{"sourceId":7458672,"sourceType":"datasetVersion","datasetId":4341534},{"sourceId":7459017,"sourceType":"datasetVersion","datasetId":4341645}],"dockerImageVersionId":30733,"isInternetEnabled":true,"language":"python","sourceType":"script","isGpuEnabled":true},"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3.10.13","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"class MarkerHandler(HandlerLine2D):\n    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):\n        line = plt.Line2D([width/2], [height/2], ls=\"\", marker=orig_handle.get_marker(),\n                          color=orig_handle.get_color(), markersize=orig_handle.get_markersize())\n        return [line]  \n\nplt.rcParams.update({\n    'axes.facecolor': '#f2f2f2',  \n    'axes.edgecolor': 'white',\n    'axes.grid': True,\n    'grid.color': 'white',\n    'grid.linestyle': '--',  \n    'font.size': 12  \n})\n\n\n# Adjust parameters parameters below:\nnpaths=1000000\nn_paths = range(1)\nk_list = np.linspace(0,1,500)\n\nNIG_WeeklyHedgeError_diffk = []\ncvars_sa = []  \n\nfor k in k_list:\n\n    NIG_WeeklyHedgeError = NIG_Delta_gamma_HedgeErrors(Weeklypaths_NIG, Strike, Gamma_greek_c, Gamma_greek_d, Delta_greek_c, Delta_greek_d,\n                                 D_d, D_e, r, T_d, dt_weekly, isput, NIG_InitCapital, k )\n\n    NIG_WeeklyHedgeError_diffk.append(NIG_WeeklyHedgeError)\n\n    NIG_WeeklyHedgeError_array = np.array(NIG_WeeklyHedgeError)\n\n    var_weekly = var_sa(NIG_WeeklyHedgeError, alph)\n\n    NIG_WeeklyHedgeError1 = [NIG_WeeklyHedgeError]\n    NIG_WeeklyHedgeError1 = np.reshape(NIG_WeeklyHedgeError1, (1,1,npaths))\n    \n    CVaR_HedgeError_evt2 = get_cvars_sa(NIG_WeeklyHedgeError1, alph, sampsizes)\n    cvars_sa.append(CVaR_HedgeError_evt2[0])\n    \n    \ncvarss_sa = []\nfor i in range(len(cvars_sa)):\n    aa = cvars_sa[i][0][0][0]\n    cvarss_sa.append(aa)\n    \n\n\nplt.figure(figsize=(8, 6))\nplt.plot(k_list, cvarss_sa)\nplt.xlabel('$θ$', fontsize=14)\nplt.ylabel('$CVaR_{0.999}$', fontsize=14)\ny_min = np.min(cvarss_sa)\nx_min = k_list[np.argmin(cvarss_sa)]\nline, = plt.plot(x_min, y_min, marker='o', markersize=6, color='red', label='Optimal value')\n\n\nplt.legend(handler_map={line: MarkerHandler()})\nplt.tight_layout()\nplt.savefig('cvarss_sa.pdf')\nprint(f'Minimum point of CVaR_EVT is {y_min} with k {x_min}')","metadata":{"_uuid":"b1463029-fcc3-412d-85da-8e586541b657","_cell_guid":"a7c8a2f8-8c69-4a23-86bd-2270a212711e","collapsed":false,"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2024-06-23T23:08:23.321992Z","iopub.execute_input":"2024-06-23T23:08:23.322392Z","iopub.status.idle":"2024-06-23T23:08:23.335328Z","shell.execute_reply.started":"2024-06-23T23:08:23.322353Z","shell.execute_reply":"2024-06-23T23:08:23.334275Z"},"trusted":true},"execution_count":1,"outputs":[{"traceback":["\u001b[0;36m  Cell \u001b[0;32mIn[1], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    class MarkerHandler(HandlerLine2D):\u001b[0m\n\u001b[0m                                       ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m incomplete input\n"],"ename":"SyntaxError","evalue":"incomplete input (163669016.py, line 1)","output_type":"error"}]}]}