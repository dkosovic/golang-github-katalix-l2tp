# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/katalix/go-l2tp
%global goipath         github.com/katalix/go-l2tp
Version:                0.1.8

%gometa -f

%global common_description %{expand:
Go library for building L2TP applications on Linux systems.}

%global golicenses      LICENSE
%global godocs          doc CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go library for building L2TP applications on Linux systems

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

Provides:       go-l2tp = %{version}-%{release}

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                                                     %{buildroot}%{_sbindir}
install -m 0755 -vp %{gobuilddir}/bin/*                                 %{buildroot}%{_sbindir}/
install -m 0755 -vd                                                     %{buildroot}%{_mandir}/man8
install -m 0644 -vp %{_builddir}/go-l2tp-%{version}/doc/kl2tpd.8        %{buildroot}%{_mandir}/man8
install -m 0644 -vp %{_builddir}/go-l2tp-%{version}/doc/kpppoed.8       %{buildroot}%{_mandir}/man8
install -m 0644 -vp %{_builddir}/go-l2tp-%{version}/doc/ql2tpd.8        %{buildroot}%{_mandir}/man8
install -m 0755 -vd                                                     %{buildroot}%{_mandir}/man5
install -m 0644 -vp %{_builddir}/go-l2tp-%{version}/doc/kl2tpd.toml.5   %{buildroot}%{_mandir}/man5
install -m 0644 -vp %{_builddir}/go-l2tp-%{version}/doc/ql2tpd.toml.5   %{buildroot}%{_mandir}/man5

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_sbindir}/kl2tpd
%{_sbindir}/kpppoed
%{_sbindir}/ql2tpd
%{_mandir}/man{8,5}/*.{8,5}*

%gopkgfiles

%changelog
%autochangelog
