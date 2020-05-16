# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['kathara.py'],
             pathex=['../src/'],
             binaries=[],
             datas=[],
             hiddenimports=['Resources',
                            'Resources.cli.command',
                            'Resources.cli.command.CheckCommand',
                            'Resources.cli.command.ConnectCommand',
                            'Resources.cli.command.ExecCommand',
                            'Resources.cli.command.LcleanCommand',
                            'Resources.cli.command.LinfoCommand',
                            'Resources.cli.command.ListCommand',
                            'Resources.cli.command.LrestartCommand',
                            'Resources.cli.command.LstartCommand',
                            'Resources.cli.command.LtestCommand',
                            'Resources.cli.command.LconfigCommand',
                            'Resources.cli.command.SettingsCommand',
                            'Resources.cli.command.VcleanCommand',
                            'Resources.cli.command.VconfigCommand',
                            'Resources.cli.command.VstartCommand',
                            'Resources.cli.command.WipeCommand',
                            'Resources.cli.ui.setting.DockerOptionsHandler',
                            'Resources.cli.ui.setting.KubernetesOptionsHandler',
                            'Resources.manager.ManagerProxy',
                            'Resources.manager.docker.DockerManager'
                            'Resources.manager.kubernetes.KubernetesManager',
                            'Resources.setting.addon.DockerSettingsAddon',
                            'Resources.setting.addon.KubernetesSettingsAddon'
                            ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='kathara',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='app_icon.ico'
           )