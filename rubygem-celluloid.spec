#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-celluloid
Version  : 0.16.0
Release  : 5
URL      : https://rubygems.org/downloads/celluloid-0.16.0.gem
Source0  : https://rubygems.org/downloads/celluloid-0.16.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-benchmark_suite
BuildRequires : rubygem-bundler
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-docile
BuildRequires : rubygem-domain_name
BuildRequires : rubygem-guard-rspec
BuildRequires : rubygem-hitimes
BuildRequires : rubygem-http-cookie
BuildRequires : rubygem-mime-types
BuildRequires : rubygem-netrc
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rest-client
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-rubocop
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html
BuildRequires : rubygem-term-ansicolor
BuildRequires : rubygem-thor
BuildRequires : rubygem-timers
BuildRequires : rubygem-tins
BuildRequires : rubygem-unf
BuildRequires : rubygem-unf_ext

%description
![Celluloid](https://raw.github.com/celluloid/celluloid-logos/master/celluloid/celluloid.png)
=========
[![Gem Version](https://badge.fury.io/rb/celluloid.png)](http://rubygems.org/gems/celluloid)
[![Build Status](https://secure.travis-ci.org/celluloid/celluloid.png?branch=master)](http://travis-ci.org/celluloid/celluloid)
[![Code Climate](https://codeclimate.com/github/celluloid/celluloid.png)](https://codeclimate.com/github/celluloid/celluloid)
[![Coverage Status](https://coveralls.io/repos/celluloid/celluloid/badge.png?branch=master)](https://coveralls.io/r/celluloid/celluloid)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n celluloid-0.16.0
gem spec %{SOURCE0} -l --ruby > rubygem-celluloid.gemspec

%build
gem build rubygem-celluloid.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
celluloid-0.16.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/celluloid-0.16.0
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/celluloid-0.16.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/actor.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/actor_system.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/autostart.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/call_chain.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/calls.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/cell.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/condition.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/core_ext.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/cpu_counter.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/evented_mailbox.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/exceptions.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/fiber.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/fsm.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/future.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/handlers.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/internal_pool.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/legacy.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/links.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/logger.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/logging.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/logging/incident.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/logging/incident_logger.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/logging/incident_reporter.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/logging/log_event.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/logging/ring_buffer.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/mailbox.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/method.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/notifications.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/pool_manager.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/probe.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/properties.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/proxies/abstract_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/proxies/actor_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/proxies/async_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/proxies/block_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/proxies/cell_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/proxies/future_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/proxies/sync_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/receivers.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/registry.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/responses.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/rspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/rspec/actor_examples.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/rspec/example_actor_class.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/rspec/mailbox_examples.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/rspec/task_examples.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/signals.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/stack_dump.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/supervision_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/supervisor.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/system_events.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/task_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/tasks/task_fiber.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/tasks/task_thread.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/test.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/thread.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/thread_handle.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/lib/celluloid/uuid.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/actor_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/actor_system_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/block_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/calls_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/condition_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/cpu_counter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/evented_mailbox_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/fsm_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/future_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/internal_pool_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/links_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/logging/ring_buffer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/mailbox_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/notifications_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/pool_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/probe_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/properties_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/registry_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/stack_dump_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/supervision_group_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/supervisor_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/tasks/task_fiber_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/tasks/task_thread_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/thread_handle_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/timer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/celluloid/uuid_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/celluloid-0.16.0/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/celluloid-0.16.0.gemspec
